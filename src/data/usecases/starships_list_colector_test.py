from src.infra import SwapApiConsumer

from .starships_list_colector import StarShipsListColector


def test_list():
    api_consumer = SwapApiConsumer()
    starships_list_colector = StarShipsListColector(api_consumer)

    page = 1
    starships_list_colector.list(page)
