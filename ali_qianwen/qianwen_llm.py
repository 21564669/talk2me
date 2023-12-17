# -*- coding: utf-8 -*-
from http import HTTPStatus
import dashscope
import os
import json
import config as c
from qianwen_text_to_audio import qwen_text_audio

dashscope.api_key = c.ali_qw_key
response = dashscope.Generation.call(
    model='qwen-max',
    prompt="I want to set up a company that uses the natural enemies of pests to prevent and control pests, and does overall biological control and integrated biological control. Can you help me choose 5 names for the company and products? I'll choose.",
    seed=7656,
    top_p=0.8,
    result_format='message',
    enable_search=False,
    max_tokens=1500,
    temperature=1.0,
    repetition_penalty=1.0
)
if response.status_code == HTTPStatus.OK:
    content = response.output.choices[0].message.content
    if content:
        print(content)
        for model in c.audio_model_list:
            qwen_text_audio(content, model=model, output_path=rf'.\ali_qianwen\audio_result\{model}.mp3')
else:
    print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
        response.request_id, response.status_code,
        response.code, response.message
    ))