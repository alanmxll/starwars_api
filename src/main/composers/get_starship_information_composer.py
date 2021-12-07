from src.data.usecases import StarshipInformationCollector
from src.infra import SwapiApiConsumer
from src.presenters.controllers import StarshipInformationCollectorController


def get_starship_information_composer():
    ''' Composer '''

    infra = SwapiApiConsumer()
    usecase = StarshipInformationCollector(infra)
    controller = StarshipInformationCollectorController(usecase)

    return controller
