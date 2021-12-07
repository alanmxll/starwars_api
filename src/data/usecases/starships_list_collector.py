from typing import Dict, List, Type

from src.data.interfaces import SwapiApiConsumerInterface
from src.domain.usecases import StarshipsListCollectorInterface


class StarshipsListCollector(StarshipsListCollectorInterface):
    ''' StarshipsListCollector usecase '''

    def __init__(self, api_consumer: Type[SwapiApiConsumerInterface]) -> None:
        self.__api_consumer = api_consumer

    def list(self, page: int) -> List[Dict]:
        '''
            List some starships informations
            :params - page: int with the number in pagination
            :returns - List with all information
        '''

        api_response = self.__api_consumer.get_starships(page)
        starships_formatted_list = self.__format_api_response(
            api_response.response["results"])
        return starships_formatted_list

    @classmethod
    def __format_api_response(cls, results: List[Dict]):
        '''
            Format response from api
            :params - results: List with spaceships informations
            :returns - List with spaceships informations formated
        '''

        starships_formatted_list = []

        for starship in results:
            starships_formatted_list.append(
                {
                    "id": starship["url"].split("/")[-2],
                    "name": starship["name"],
                    "model": starship["model"],
                    "max_atmosphering_speed": starship["max_atmosphering_speed"],
                    "hyperdrive_rating": starship["hyperdrive_rating"],
                    "MGLT": starship["MGLT"]
                }
            )

        return starships_formatted_list
