from abc import ABC, abstractclassmethod
from typing import Dict, List


class StarShipsListColectorInterface(ABC):
    """Starships Colector Interface"""

    @abstractclassmethod
    def list(self, page: int) -> List[Dict]:
        """Para ser implementado"""
        raise Exception("Deve implementar o metodo de lista.")
