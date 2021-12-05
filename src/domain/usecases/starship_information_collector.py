from abc import ABC, abstractmethod
from typing import Dict


class StarshipsInformationCollectorInterface(ABC):
    ''' Starship Information Collector Interface '''
    @abstractmethod
    def find_starship(self, starship_id: int, time: str) -> Dict:
        ''' Must Implement '''
        raise Exception('Must implement find_starship method')
