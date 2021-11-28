import requests


class SwapiApiConsumer:
    @classmethod
    def get_starships(self, page: int) -> any:
        params = {'page': page}
        response = requests.get('https://swapi.dev/api/star`ships/', params=params)

        return response.json()
