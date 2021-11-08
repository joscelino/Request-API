from collections import namedtuple
from typing import Dict, Tuple, Type

import requests
from requests import Request

from src.errors import HttpRequestError


class SwapApiConsumer:

    """Class to consume swapi api with http requests"""

    def __init__(self) -> None:
        self.get_starships_response = namedtuple(
            "GET_Starships", "status_code request response"
        )

    def get_starships(self, page: int) -> Tuple[int, Type[Request], Dict]:
        """Request starships nas paginacoes.

        Args:
            page (int): numero inteiro da pagina de navegacao.

        Raises:
            HttpRequestError: Erros de requisicao

        Returns:
            Tuple[int, Type[Request], Dict]: tupla com status code, request e
            response.
        """

        req = requests.Request(
            method="GET", url="https://swapi.dev/api/starships/", params={"page": page}
        )
        req_prepared = req.prepare()
        response = self.__send_http_requests(req_prepared)
        status_code = response.status_code

        if status_code >= 200 and status_code <= 299:
            return self.get_starships_response(
                status_code=status_code, request=req, response=response.json()
            )
        else:
            raise HttpRequestError(
                message=response.json()["detail"], status_code=status_code
            )

    @classmethod
    def __send_http_requests(cls, req_prepared: Type[Request]) -> any:
        """Prepara a sessao e envia a requisicao http.

        Args:
            req_prepared (Type[Request]): Objeto de requisicao com todos
            os parametros

        Returns:
            any: resposta da requisicao HTTP
        """
        http_session = requests.Session()
        response = http_session.send(req_prepared)
        return response
