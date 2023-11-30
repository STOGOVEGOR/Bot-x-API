from flask import Flask, request
from flask_cors import CORS

from base_route.api_routes import RegisterUserRoute, AuthenticateUserRoute

from utils.services import make_proxy_request, make_out_response

from constants.https_methods import HTTPMethods
from constants.uri_dispatch import URIDispatch

from base_route.api_routes import BotList

app = Flask(__name__)
CORS(app)

PREFIX = '/api/v0'


@app.route(f'{PREFIX}/{URIDispatch.REGISTER}', methods=["POST"])
def register_user():
    data = request.get_json()
    response = make_proxy_request(RegisterUserRoute, data,
                                  HTTPMethods.POST, URIDispatch.REGISTER)

    out_response = make_out_response(response)
    return out_response


@app.route(f'{PREFIX}/{URIDispatch.LOGIN}', methods=["POST"])
def authenticate_user():
    data = request.get_json()
    response = make_proxy_request(AuthenticateUserRoute, data,
                                  HTTPMethods.POST, URIDispatch.LOGIN)

    out_response = make_out_response(response)
    return out_response


@app.route(f'{PREFIX}/bots', methods=["GET"])
def get_bots():
    response = make_proxy_request(BotList, {},
                                  HTTPMethods.GET, "bots")

    out_response = make_out_response(response)
    return out_response


if __name__ == '__main__':
    app.run(debug=True)
