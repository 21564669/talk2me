from typing import List
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatMessagePromptTemplate
from qianwen_llm import QianwenLLM
from qianwen_text_to_audio import QianwenText2Audio
from fastapi import FastAPI
from langserve import add_routes
import uvicorn



if __name__ == "__main__":
    template = """You are a helpful assistant who identify any error of the english.
    A user will pass in one or more setences,
    and you should identify whether there are any error in english in the input,
    and provides some suggestions to fix the error and explain why.
    you need toreturn a string type object."""
    human_template = "{text}"
    chat_prompt = ChatMessagePromptTemplate.format_messages([
        ("system", template),
        ("human", human_template),
    ])
    LLM_SERVER_IP = "localhost"
    chat = ChatOpenAI(model='gpt-3.5-turbo', model_name="gpt-3.5-turbo", openai_api_key="empty", openai_api_base=f"http://{LLM_SERVER_IP}:8000/v1")
    chain = chat_prompt|chat|QianwenLLM()|QianwenText2Audio()
    print(chain.invoke({"text":"""
            The larger land animal in Earth, know for it's long trunk, large ear, and tusk.
            A domesticated mammal common kept as a pet, know for it's loyalty and affection above human.
"""}))

    app = FastAPI(
        title="LangChain Server",
        version="1.0",
        description="A simple API server using LangChain's Runnable interfaces",
    )

    add_routes(
        app,
        chain,
        path="/english_chain"
    )
    uvicorn.run(app, host="localhost", port=8000)