# from fastapi import Depends

# from ..service import Service, get_service
# from . import router


# @router.get("/{id}", status_code=200)
# def get_advertisement(
#     id: str,
#     svc: Service = Depends(get_service),
# ):
#     """
#     Retrieves the advertisement with the given ID.
#     """
#     advertisement = svc.repository.get_shanyraq(id)

#     # If the advertisement is not found, you can return an appropriate response
#     if advertisement is None:
#         return {"msg": "Advertisement not found"}

#     # Construct the response payload with the advertisement details and image URLs
#     response = {
#         "_id": id,
#         # "type": advertisement.type,
#         # "price": advertisement.price,
#         # "address": advertisement.address,
#         # "area": advertisement.area,
#         # "rooms_count": advertisement.rooms_count,
#         # "description": advertisement.description,
#         # "user_id": advertisement.user_id,
#         # "media": [],
#     }

#     # Add the image URLs to the response
#     for media_url in advertisement.media:
#         response["media"].append(media_url)

#     return response
