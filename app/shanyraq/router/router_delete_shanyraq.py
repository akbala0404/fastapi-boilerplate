# from typing import Any

from fastapi import Depends, Response

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data

from ..service import Service, get_service

from . import router


@router.delete("/{question_id:str}")
def delete_shanyraq(
    question_id: str,
    svc: Service = Depends(get_service),
) -> dict[str, str]:
    delete_result = svc.repository.delete_shanyraq(question_id)
    if delete_result.deleted_count == 1:
        return Response(status_code=200)
    return Response(status_code=404)