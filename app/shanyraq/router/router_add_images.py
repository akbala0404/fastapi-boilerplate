from fastapi import Depends, UploadFile
from typing import List
from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from ..service import Service, get_service
from . import router


@router.post("/file")
def upload_file(
    file: UploadFile,
    svc: Service = Depends(get_service),
):
    """
    file.filename: str - Название файла
    file.file: BytesIO - Содержимое файла
    """
    url = svc.s3_service.upload_file(file.file, file.filename)
    
    return {"msg": url}


@router.post("/files")
def upload_files(
    files: List[UploadFile],
    svc: Service = Depends(get_service),
):
    """
    file.filename: str - Название файла
    file.file: BytesIO - Содержимое файла
    """
    
    result = []
    for file in files:
        url = svc.s3_service.upload_file(file.file, file.filename)
        result.append(url)
    
    return {"msg": files}


@router.post("/{id}/media", status_code=200)
def upload_files_to_shanyraq(
    id: str,
    files: List[UploadFile],
    svc: Service = Depends(get_service),
    jwt_data: JWTData = Depends(parse_jwt_user_data),

):
    result = []
    for file in files:
        url = svc.s3_service.upload_file(file.file, file.filename)
        result.append(url)

    svc.repository.add_images_to_shanyraq(id, jwt_data.user_id, result)
    return {"msg": "Files uploaded successfully", "urls": result}
