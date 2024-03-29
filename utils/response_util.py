import json

from core.ResultBase import ResultResponse
from utils.log_util import logger


def process_response(response):
    if response.status_code == 200 or response.status_code == 201 or response.status_code == 204:
        ResultResponse.success = True
        ResultResponse.body = response.json()

    elif response.stauts == 200 or response.stauts == 201 or response.stauts == 204:
        ResultResponse.success = True
        ResultResponse.body = response.json()
    else:
        ResultResponse.success = False
        logger.info("接口状态码不是2开头，请检查" + response.status_code)
    logger.info("接口的返回内容>>>：" + json.dumps(response.json(), ensure_ascii=False))
    return ResultResponse
