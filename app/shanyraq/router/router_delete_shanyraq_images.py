# from typing import Any

from fastapi import Depends, Response

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data

from ..service import Service, get_service

from . import router


@router.delete("/{shanyraq_id:str}/media")
def delete_shanyraq(
    shanyraq_id: str,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> Response:
    update_result = svc.repository.delete_media_from_shanyraq(
        shanyraq_id, jwt_data.user_id)
    if update_result.modified_count == 1:
        return Response(status_code=200)
    return Response(status_code=404)