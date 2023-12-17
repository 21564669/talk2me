import dashscope
from dashscope.audio.tts import SpeechSynthesizer
import config as c
dashscope.api_key = c.ali_qw_key

def qwen_text_audio(text, model, sample_rate=48000, output_path="output.mp3"):
    result = SpeechSynthesizer.call(model=model,
                                    text=text,
                                    sample_rate=sample_rate)
    if result.get_audio_data() is not None:
        with open(output_path, 'wb') as f:
            f.write(result.get_audio_data())