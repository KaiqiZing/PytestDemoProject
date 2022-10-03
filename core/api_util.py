from core.rest_client import RestClient


#配置路由方法和地址，并获取到api传入的参数
# def get_mobile_belong(**kwargs):
#     return get("/shouji/query",**kwargs)


class Api(RestClient):
    def __init__(self):
        super().__init__()
    def get_mobile_belong(self,**kwargs):
        return self.get("/shouji/query", **kwargs)


    def post_data(self, **kwargs):
        return self.post("/posts", **kwargs)

api_utils = Api()