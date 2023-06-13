from fastapi import Depends, HTTPException, status

from app.utils import AppModel

from ..service import Service, get_service
from . import router


class CreateListingRequest(AppModel):
    type: str
    price: int
    address: str
    area: float
    rooms_count: int
    description: str


class CreateListingResponse(AppModel):
    _id: str


@router.post(
    "/shanyraks/",
    status_code=status.HTTP_201_CREATED,
    response_model=CreateListingResponse,
)
def create_listing(
    request: CreateListingRequest,
    svc: Service = Depends(get_service),
) -> CreateListingResponse:
    user_id = svc.get_current_user().user_id
    listing_data = request.dict()
    listing_data["user_id"] = user_id

    listing_id = svc.create_listing(listing_data)

    return CreateListingResponse(_id=str(listing_id))
