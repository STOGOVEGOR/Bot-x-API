from base_route.base_route import BaseRoute


class BotList(BaseRoute):
    uri = "bots"

    def prepare_response(self, response):
        for item in response['result']:
            del(item["available"])
            del(item["status_code"])
            item["model"] = "Bot"

        super().prepare_response(response)


