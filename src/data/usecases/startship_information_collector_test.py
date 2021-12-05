import re
from typing import Dict
from src.data .usecases import StarshipInformationCollector
from src.infra.test import SwapiApiConsumerSpy


def test_find_starship():
    ''' Testing find_starship method '''

    api_consumer = SwapiApiConsumerSpy()
    starship_information_collector = StarshipInformationCollector(api_consumer)

    starship_id = 9
    time = 4

    response = starship_information_collector.find_starship(starship_id, time)

    assert api_consumer.get_starships_information_attributes['starship_id'] == starship_id
    assert isinstance(response, dict)
    assert 'MGLT' in response
    assert 'distance_traveled' in response
