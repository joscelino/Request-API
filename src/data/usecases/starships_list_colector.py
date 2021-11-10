from typing import Dict, List, Type

from src.data.interfaces import SwapiAPiConsumerInterface
from src.domain.usecases import StarShipsListColectorInterface


class StarShipsListColector(StarShipsListColectorInterface):

    """StarShipsListColector usecase."""

    def __init__(self, api_consumer: Type[SwapiAPiConsumerInterface]) -> None:
        self.__api_consumer = api_consumer

    def list(self, page: int) -> List[Dict]:
        response = self.__api_consumer.get_starships(page)
        print(response)
