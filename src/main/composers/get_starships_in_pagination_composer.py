from src.infra import SwapiApiConsumer
from src.data.usecases import StarshipsListCollector
from src.presenters.controllers import StarshipsListCollectorController


def get_starships_in_pagination_composer():
    ''' Composer '''

    infra = SwapiApiConsumer()
    usecase = StarshipsListCollector(infra)
    controller = StarshipsListCollectorController(usecase)

    return controller
