from flask import Flask, request, Response

from base_route.api_routes import RegisterUserRoute, AuthenticateUserRoute, \
    DeactivateUserRoute, CheckEmailStatusRoute, \
    VerifyEmailRoute, ReverifyEmailRoute

from services import make_proxy_request, make_out_response

from constants.https_methods import HTTPMethods
from constants.uri_dispatch import URIDispatch

app = Flask(__name__)

PREFIX = '/api/v0'

MY_PREFIX = 'users'


@app.route(f'{PREFIX}/{MY_PREFIX}', methods=["POST"])
def register_user():
    data = request.get_json()
    response = make_proxy_request(RegisterUserRoute, data,
                                  HTTPMethods.POST, URIDispatch.REGISTER)

    out_response = make_out_response(response)
    return out_response


@app.route(f'{PREFIX}/users/login', methods=["POST"])
def authenticate_user():
    data = request.get_json()
    response = make_proxy_request(AuthenticateUserRoute, data,
                                  HTTPMethods.POST, URIDispatch.LOGIN)

    out_response = make_out_response(response)
    return out_response


if __name__ == '__main__':
    app.run(port=8000,debug=True)
