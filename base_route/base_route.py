import json

import requests


class BaseRoute:
    APP_ID = '2750bc42-702e-4cbe-bae5-798f171389e1'
    APP_URL = 'http://core.webstktw.beget.tech/api/v0/apps/{}'.format(APP_ID)

    parameters: str = ''

    response = None

    def get_parameters(self):
        return self.parameters

    def prepare_parameters(self, parameters: dict):
        self.parameters = parameters

    def send(self, uri: str, method: str = 'GET'):
        url = '{}/{}'.format(self.APP_URL, uri)
        r = requests.request(method, url, data=self.parameters)
        self.prepare_response(r)

    def get_response(self):
        return self.response

    def prepare_response(self, response: str):
        self.response = response
