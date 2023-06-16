# from fastapi import Depends
# # from typing import List
# from app.auth.adapters.jwt_service import JWTData
# from app.auth.router.dependencies import parse_jwt_user_data
# from ..service import Service, get_service
# from . import router


# @router.post("/{id}/comments", status_code=200)
# def add_comments_to_shanyraq(
#     id: str,
#     content: str,
#     svc: Service = Depends(get_service),
#     jwt_data: JWTData = Depends(parse_jwt_user_data),

# ):
#     svc.repository.add_images_to_shanyraq(id, jwt_data.user_id, result)
#     return {"msg": "Files uploaded successfully", "urls": result}
