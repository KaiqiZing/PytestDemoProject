from core.rest_client import get


#配置路由方法和地址，并获取到api传入的参数
def get_mobile_belong(params, **kwargs):
    return get("/shouji/query", params, **kwargs)
