from core.rest_client import RestClient


# 配置总的路由地址，通过该地址访问基于request封装的接口
# def get_mobile_belong(**kwargs):
#     return get("/shouji/query",**kwargs)


class Api(RestClient):
    def __init__(self):
        super().__init__()
    def get_mobile_belong(self,**kwargs):
        return self.get("/shouji/query", **kwargs)


    def post_data(self, **kwargs):
        return self.post("/posts", **kwargs)


    # 以下项目实战的地址
    def get_code(self, **kwargs):
        return self.post("/code/", **kwargs)

    def register_mobile(self, **kwargs):
        return self.post("/users/", **kwargs)

    def user_login(self, **kwargs):
        return self.post("/login/", **kwargs)

    def shopping_add(self, **kwargs):
        return self.post("/shopcarts/", **kwargs)


    # 查询banner
    def banner(self, **kwargs):
        return self.get("/banners/", **kwargs)

    def elamin(self, **kwargs):
        return self.get("/auth/info/", **kwargs)

    def elamin_usercenter(self, **kwargs):
        return self.put("/api/users/center/", **kwargs)
api_utils = Api()