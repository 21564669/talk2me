from http import HTTPStatus
from urllib.parse import urlparse, unquote
from pathlib import PurePosixPath
import requests
import dashscope
import os

dashscope.api_key = os.environ.get("ali_qw_key")
def simple_call():
    prompt = "python编程语言的logo，做成的卡通头像"
    rsp = dashscope.ImageSynthesis.call(model=dashscope.ImageSynthesis.Models.wanx_v1,
                              prompt=prompt,
                              n=4,
                              size='1024*1024')
    if rsp.status_code == HTTPStatus.OK:
        print(rsp.output)
        print(rsp.usage)
        # save file to current directory
        for index, result in enumerate(rsp.output.results, start=1):
            file_name = PurePosixPath(unquote(urlparse(result.url).path)).parts[-1]
            with open(f"{prompt}_{index}_{file_name}", 'wb+') as f:
                f.write(requests.get(result.url).content)
    else:
        print('Failed, status_code: %s, code: %s, message: %s' %
              (rsp.status_code, rsp.code, rsp.message))


if __name__ == '__main__':
    simple_call()