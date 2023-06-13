from typing import Any
from pydantic import Field
from fastapi import Depends, HTTPException, status
from app.utils import AppModel
from ..adapters.jwt_service import JWTData
from ..service import Service, get_service
from . import router
from .dependencies import parse_jwt_user_data


class GetMyAccountResponse(AppModel):
    id: Any = Field(alias="_id")
    email: str
    phone: str
    name: str
    city: str


@router.get("/users/me", response_model=GetMyAccountResponse)
def get_my_account(
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> GetMyAccountResponse:
    user = svc.repository.get_user_by_id(jwt_data.user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return GetMyAccountResponse(**user)

