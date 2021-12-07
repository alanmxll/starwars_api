from typing import Dict, Type

from src.domain.usecases import StarshipsInformationCollectorInterface
from src.presenters.interface import ControllersInterface


class StarshipInformationCollectorController(ControllersInterface):
    ''' Controller to StarshipInformationCollector'''

    def __init__(self, starship_information_collector: Type[StarshipsInformationCollectorInterface]) -> None:
        self.__usecase = starship_information_collector

    def handler(self, http_request: Dict):
        ''' Handle to information collector controller '''

        starship_id = http_request["body"]["starship_id"]
        time = http_request["body"]["time"]

        starship_information = self.__usecase.find_starship(starship_id, time)
        http_response = {"status_code": 200,
                         "data": {"data": starship_information}}

        return http_response
