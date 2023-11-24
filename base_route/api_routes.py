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
        res = json.loads(response._content)
        for item in res['result']:
            # del(item["available"])
            # del(item["status_code"])
            item["code"] = item["name"]
            item["model_name"] = None
            item["mode_name"] = None
            if 'gpt' in item["name"]:
                tmp_list = item["name"].split('-')
                item["name"] = 'ChatGPT'
                item["model_name"] = f"{tmp_list[0].capitalize()}-{tmp_list[1]}"
                item["mode_name"] = f"{tmp_list[-1]} context"

        response._content = json.dumps(res)
        super().prepare_response(response)

