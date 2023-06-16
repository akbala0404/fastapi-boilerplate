from app.config import database
from pydantic import BaseSettings
# from .adapters.here_service import HereService
from .repository.repository import ShanyraqRepository
from .adapters.s3_service import S3Service


class Config(BaseSettings):
    HERE_API_KEY: str


class Service:
    def __init__(self, repository: ShanyraqRepository):
        # config = Config()        
        self.repository = repository
        self.s3_service = S3Service()
        # self.here_service = HereService(config.HERE_API_KEY)


def get_service():
    repository = ShanyraqRepository(database)
    return Service(repository)
