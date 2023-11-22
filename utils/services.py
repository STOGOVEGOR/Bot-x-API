from flask import Response

from base_route.base_route import BaseRoute


def make_proxy_request(route_class: BaseRoute,
                       data: dict = {},
                       method: str = 'GET',
                       uri: str = None) -> Response:
    route = route_class()
    route.prepare_parameters(data)
    route.send(uri, method)
    response = route.get_response()
    return response


def make_out_response(response: Response) -> Response:
    headers = dict(response.raw.headers)
    status = response.status_code
    out_response = Response(response=response, status=status, headers=headers)
    return out_response
