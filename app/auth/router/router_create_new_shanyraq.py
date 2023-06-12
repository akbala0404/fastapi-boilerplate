from fastapi import Depends, HTTPException, status
from app.utils import AppModel
from ..adapters.jwt_service import JWTData
from ..service import Service, get_service
from . import router
from .dependencies import parse_jwt_user_data


class CreateListingRequest(AppModel):
    type: str
    price: int
    address: str
    area: float
    rooms_count: int
    description: str


class CreateListingResponse(AppModel):
    _id: str


@router.post("/shanyraks/", response_model=CreateListingResponse)
def create_listing(
    request: CreateListingRequest,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> CreateListingResponse:
    user_id = jwt_data.user_id
    listing_data = request.dict()
    listing_data["user_id"] = user_id

    listing_id = svc.repository.create_listing(listing_data)

    return CreateListingResponse(_id=listing_id)
