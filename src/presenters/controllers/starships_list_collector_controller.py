from typing import Dict, Type

from src.domain.usecases import StarshipsListCollectorInterface


class StarshipsListCollectorController:
    ''' Controller to List Starships '''

    def __init__(self,  starship_list_collector: Type[StarshipsListCollectorInterface]) -> None:
        self.__use_case = starship_list_collector

    def handle(self, http_request: Dict) -> Dict:
        ''' Handler to list collector '''
        page = http_request["query_params"]["page"]
        starships_list = self.__use_case.list(page)
        http_response = {"status_code": 200, "data": starships_list}

        return http_response
