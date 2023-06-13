from pydantic import BaseSettings

from app.config import database

from .adapters.jwt_service import JwtService
from .repository.repository import AuthRepository


class AuthConfig(BaseSettings):
    JWT_ALG: str = "HS256"
    JWT_SECRET: str = "YOUR_SUPER_SECRET_STRING"
    JWT_EXP: int = 10_800


config = AuthConfig()


class Service:
    def __init__(
        self,
        auth_repository: AuthRepository,
        listing_repository: ListingRepository,
        jwt_service: JwtService,
    ):
        self.auth_repository = auth_repository
        self.listing_repository = listing_repository
        self.jwt_service = jwt_service


def get_service():
    auth_repository = AuthRepository(database)
    listing_repository = ListingRepository(database)
    jwt_service = JwtService(config.JWT_ALG, config.JWT_SECRET, config.JWT_EXP)

    service = Service(auth_repository, listing_repository, jwt_service)
    return service