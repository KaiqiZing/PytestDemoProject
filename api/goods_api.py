from core.api_util import api_utils
from utils.response_util import process_response


def get_banner():
    """

    :param json_data:
    :return:
    """
    response = api_utils.banner()
    return process_response(response)


def get_eladmin():
    cookies = {
        'cookie_name': 'Hm_lvt_300a24a5326d0e7a0ff1b14c4e8d9056=1679541530; sidebarStatus=1; Hm_lpvt_300a24a5326d0e7a0ff1b14c4e8d9056=1679989087; ELADMIN-TOEKN=Bearer%20eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIzM2QyYmU2NGMzMGE0MTc4ODlmYjE3YmRiZTZhNWU5MyIsInVzZXIiOiJhZG1pbiIsInN1YiI6ImFkbWluIn0.E-rb7JwcJjfHEawpK5PtN1AgaCFLi9LNp6048BuB3LecNb7xZXP1MBVcM6DBkVxTxJb4E4IjR-E3MVdBKlObXQ'}
    headers = {
        'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIzM2QyYmU2NGMzMGE0MTc4ODlmYjE3YmRiZTZhNWU5MyIsInVzZXIiOiJhZG1pbiIsInN1YiI6ImFkbWluIn0.E-rb7JwcJjfHEawpK5PtN1AgaCFLi9LNp6048BuB3LecNb7xZXP1MBVcM6DBkVxTxJb4E4IjR-E3MVdBKlObXQ'}

    response = api_utils.elamin(cookies=cookies, headers=headers)
    return process_response(response)

def post_usercenter():

    json_data = {
    "gender":"女",
    "id":"1",
    "nickName":"管理员10",
    "phone":"18888888888"
    }
    cookies = {
        'cookie_name': 'Hm_lvt_300a24a5326d0e7a0ff1b14c4e8d9056=1679541530; sidebarStatus=1; Hm_lpvt_300a24a5326d0e7a0ff1b14c4e8d9056=1679989087; ELADMIN-TOEKN=Bearer%20eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIzM2QyYmU2NGMzMGE0MTc4ODlmYjE3YmRiZTZhNWU5MyIsInVzZXIiOiJhZG1pbiIsInN1YiI6ImFkbWluIn0.E-rb7JwcJjfHEawpK5PtN1AgaCFLi9LNp6048BuB3LecNb7xZXP1MBVcM6DBkVxTxJb4E4IjR-E3MVdBKlObXQ'}
    headers = {
        'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIzM2QyYmU2NGMzMGE0MTc4ODlmYjE3YmRiZTZhNWU5MyIsInVzZXIiOiJhZG1pbiIsInN1YiI6ImFkbWluIn0.E-rb7JwcJjfHEawpK5PtN1AgaCFLi9LNp6048BuB3LecNb7xZXP1MBVcM6DBkVxTxJb4E4IjR-E3MVdBKlObXQ'}

    response =  api_utils.elamin_usercenter(json=json_data, cookies=cookies, headers=headers)
    print("===================", response)
    return process_response(response)
