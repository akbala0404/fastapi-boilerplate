from fastapi import APIRouter, Depends, status
from app.utils import AppModel
from pydantic import Field
from typing import Any
from ..service import Service, get_service
from . import router
import json


class ChatRequest(AppModel):
    prompt: str

class ChatResponse(AppModel):
    response: str

@router.post("/", response_model=ChatResponse)
def chat_with_ai(
    request: ChatRequest,
    svc: Service = Depends(get_service),
) -> ChatResponse:
    prompt = request.prompt
    if "create a game" in prompt.lower():
        response = ("Sure! Please provide more details about the game you would like to create. To generate personalized creative play ideas for your child, please provide the following details:\n\n"
                    "Child's Age:\n"
                    "Child's Interests or Hobbies:\n"
                    "Developmental Stage or Milestones:\n"
                    "Duration or Time Available for Play:\n"
                    "Preferred Indoor or Outdoor Activities:\n"
                    "Any Specific Themes or Topics of Interest:")

        content_text = response
    else:
        response = svc.chat_service.get_response(prompt)
        content_text = response["content"]
    return ChatResponse(response=content_text)


@router.post("/createGame", response_model=ChatResponse)
def chat_to_createGame(
    request: ChatRequest,
    svc: Service = Depends(get_service),
) -> ChatResponse:
    prompt = request.prompt
    if "Придумай игру" in prompt.lower():
        response = ("Конечно! Пожалуйста, предоставьте более подробные сведения о игре, которую вы хотели бы создать. Чтобы сгенерировать персонализированные творческие игровые идеи для вашего ребенка, предоставьте следующие сведения:\n\n"
                    "Возраст ребенка:\n"
                    "Интересы или увлечения ребенка:\n"
                    "Стадия развития или вехи в развитии:\n"
                    "Длительность или доступное время для игры:\n"
                    "Предпочитаемые внутренние или наружные занятия:\n"
                    "Любые конкретные темы или интересы:")

        content_text = response
    else:
        response = svc.chat_service.get_game(prompt)
        content_text = response["content"]
    return ChatResponse(response=content_text)
