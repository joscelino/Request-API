from abc import ABC, abstractmethod
from typing import Dict, Tuple, Type

from requests import Request


class SwapiAPiConsumerInterface(ABC):
    """Interface da API consumer."""

    @abstractmethod
    def get_starships(self, page: int) -> Tuple[int, Type[Request], Dict]:
        """Deve ser implementado."""
        raise Exception("Obrigatoria a implementacao do metodo!")
