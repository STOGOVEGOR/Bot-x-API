import json
from base_route.base_route import BaseRoute


class RegisterUserRoute(BaseRoute):
    pass


class AuthenticateUserRoute(BaseRoute):
    pass


class DeactivateUserRoute(BaseRoute):
    pass


class CheckEmailStatusRoute(BaseRoute):
    pass


class VerifyEmailRoute(BaseRoute):
    pass


class ReverifyEmailRoute(BaseRoute):
    pass


class BotList(BaseRoute):
    def prepare_response(self, response):
        res = json.loads(response.content)
        for item in res['result']:
            del(item["available"])
            del(item["status_code"])
            item["model"] = "Bot"

        response._content = json.dumps(res)
        super().prepare_response(response)

