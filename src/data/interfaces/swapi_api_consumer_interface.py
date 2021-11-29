from abc import ABC, abstractmethod
from typing import Dict, Tuple, Type

from requests import Request


class SwapiApiConsumerInterface(ABC):
    ''' Api consumer Interface '''

    @abstractmethod
    def get_starships(self, page: int) -> Tuple[int, Type[Request], Dict]:
        ''' Must Implement '''
        raise Exception('Must implement get_starships')
