from core.api_util import api_utils
from utils.response_util import process_response


def get_banner():
    """

    :param json_data:
    :return:
    """
    response = api_utils.banner()
    return process_response(response)
