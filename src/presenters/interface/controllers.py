from typing import Dict
from abc import ABC, abstractmethod


class ControllersInterface(ABC):
    ''' Interface to Controllers '''

    @abstractmethod
    def handler(self, http_request: Dict):
        ''' Method to handle request '''
        raise 'Should implement handle method'
