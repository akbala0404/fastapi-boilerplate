from fastapi import APIRouter, Depends, status
from app.utils import AppModel, BaseModel
from pydantic import Field
from typing import Any
from ..service import Service, get_service
from . import router
import json
import logging
import string

logging.basicConfig(level=logging.DEBUG)


class ChatRequest(AppModel):
    prompt: str

class ChatResponse(AppModel):
    response: str

class FairytaleRequest(AppModel):
    childAge: str
    childGenger: str
    storyLength: str
    mainCharacter: str
    description: str
    moralOfStory: str

class FairytaleResponse(BaseModel):
    titleOfTheFairyTale: str
    readingTime: str
    contentOfTheFairyTale: str

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
    if "/game" in prompt.lower():
        newPromt = ("Cоздай игру для моего ребенка")
        systemPromt = ("Учитывай возраст ребенка при генерации игр. Это очень важно."
                       "При разработке игры учитывайте следующие аспекты, предоставленные родителем:"
                       "- Возраст и стадия развития ребенка"
                       "- Интересы и увлечения ребенка"
                       "Желание родителя: проводить больше времени вместе или ограничить время на телефоне/компьютере"
                       "- Предпочитаемый формат игры (например, настольная игра, активность на улице, цифровая игра)"
                       "- Желаемые образовательные результаты или навыки для развития"
                       "- Возможность игры в разных средах (например, дома, в парке, во время путешествия)"
                       "Используя эту информацию, предложите концепцию игры, соответствующую требованиям родителя и приятную для ребенка. Не стесняйтесь запрашивать дополнительные детали или спецификации при необходимости.")
    #     response = ("Конечно! Пожалуйста, предоставьте более подробные сведения о игре, которую вы хотели бы создать. Чтобы сгенерировать персонализированные творческие игровые идеи для вашего ребенка, предоставьте следующие сведения:\n\n"
    #                 "Возраст ребенка:\n"
    #                 "Интересы или увлечения ребенка:\n"
    #                 "Стадия развития или вехи в развитии:\n"
    #                 "Длительность или доступное время для игры:\n"
    #                 "Предпочитаемые внутренние или наружные занятия:\n"
    #                 "Любые конкретные темы или интересы:"
    #                 "Например: Мой ребенок - девочка 5 лет. Я хотел бы придумать игру, которую мы сможем играть вместе по дороге в школу, не требуя дополнительных предметов."
    #                 "Ребенок интересуется искусством и музыкой. Она находится на стадии активного воображения и развития мелкой моторики."
    #                 " Длительность игры может быть примерно 10-15 минут. Мы предпочитаем игры, которые можно играть внутри автомобиля или просто при ходьбе. Любые темы, связанные с творчеством, музыкой или сказочным миром, будут замечательными для нас."
    #                 )

    #     content_text = response
    # else:
        response = svc.chat_service.get_game(newPromt, systemPromt)
        content_text = response["content"]
    else:
        systemPromt = ("")
        response = svc.chat_service.get_game(prompt, systemPromt)
        content_text = response["content"] 
    return ChatResponse(response=content_text)


@router.post("/createFairtale", response_model=ChatResponse)
def chat_to_createFairytale(
    request: ChatRequest,
    svc: Service = Depends(get_service),
) -> ChatResponse:
    prompt = request.prompt
    if "/fairytale" in prompt.lower():
        newPromt = ("Cоздай cказку для моего ребенка")
        systemPromt = ("Учитывай возраст ребенка при генерации сказек. Это очень важно."
                       "При разработке сказки учитывайте следующие аспекты, предоставленные родителем:"
                       "- Возраст и стадия развития ребенка"
                       "- Интересы и увлечения ребенка"
                       "Имя любимого персонажа"
                       "Любимый мультфильм или фильм"
                       "Желаемая тема сказки"
                       "Желаемый урок или смысл, который вы хотели бы, чтобы сказка несла"
                       "Используя эту информацию, предложите концепцию сказки, соответствующую требованиям родителя и приятную для ребенка. Не стесняйтесь запрашивать дополнительные детали или спецификации при необходимости.")

        response = svc.chat_service.get_fairytale(newPromt, systemPromt)
        content_text = response["content"]
    else:
        systemPromt = ("")
        response = svc.chat_service.get_fairytale(prompt, systemPromt)
        content_text = response["content"] 
    return ChatResponse(response=content_text)

# @router.post("/createFairtale2", response_model=FairytaleResponse)
# def chat_to_createFairytale2(
#     request: FairytaleRequest,
#     svc: Service = Depends(get_service),
# ) -> FairytaleResponse:
#     prompt = f"Пожалуйста, создайте сказку для ребенка {request.childAge} лет, {request.childGenger}. " \
#              f"Сказка должна быть продолжительностью {request.storyLength}. " \
#              f"Главным героем должен быть {request.description} по имени {request.mainCharacter}. " \
#              f"Мораль истории должна заключаться в том, чтобы {request.moralOfStory}."
#     systemPromt = ("")
#     response = svc.chat_service.get_fairytale(prompt, systemPromt)
#     content_text = response["content"] 
#     # data = response["content"] 
    # content_text = json.dumps(content_text, ensure_ascii=False)
#     # data = {
#     #     "titleOfTheFairyTale": "Паучий урок",
#     #     "readingTime": "15 минут",
#     #     "contentOfTheFairyTale": "Жил-был великий город, где жили много разных героев. \n\n Каждый день Питер выходил на улицу и вел борьбу с преступниками, спасая горожан от опасности."
#     # }
#     # content_text = json.dumps(data, ensure_ascii=False)
#     # inner_json = json.loads(content_text)  # Parse the inner JSON
#     # fairy_tale = FairytaleResponse(**inner_json)  # Use the inner JSON to create the FairytaleResponse object
#     # Parse the JSON data to a Python dictionary
#     data_dict = json.loads(content_text)
    
#     # Create the FairytaleResponse object directly using the data
#     fairy_tale = FairytaleResponse(data_dict)
#     return fairy_tale
#     # return ChatResponse(response=content_text)
@router.post("/createFairtale2", response_model=ChatResponse)
def chat_to_createFairytale2(
    request: FairytaleRequest,
    svc: Service = Depends(get_service),
) -> ChatResponse:
    prompt = f"Пожалуйста, создайте сказку для ребенка {request.childAge} лет, {request.childGenger}. " \
             f"Сказка должна быть продолжительностью {request.storyLength}. " \
             f"Главным героем должен быть {request.description} по имени {request.mainCharacter}. " \
             f"Мораль истории должна заключаться в том, чтобы {request.moralOfStory}."
    systemPromt = ("")
    
    # # Use the modified get_fairytale function with function calling
    response = svc.chat_service.get_fairytale(prompt, systemPromt)
    content_text = response["content"]
    # logger = logging.getLogger(__name__)

    # # Parse the JSON data to a Python dictionary
    # # data_dict = json.loads(content_text)
    # logger.debug(content_text)
    # fairy_tale = decode_fairytale_response(content_text)

    # return fairy_tale
    # print(data_dict)
    # Create the FairytaleResponse object directly using the data
    # fairy_tale = FairytaleResponse(**data_dict)
    return ChatResponse(response=content_text)
    # Use the modified get_fairytale function with function calling
    # return fairy_tale_response


@router.post("/explainTermsToChild", response_model=ChatResponse)
def chat_to_explainTermsToChild(
    request: ChatRequest,
    svc: Service = Depends(get_service),
) -> ChatResponse:
    prompt = request.prompt
    if "/explainChild" in prompt.lower():
        newPromt = ("Ты родитель и тебе нудно обьяснить одну тему для ребенка")
        systemPromt = ("Учитывай возраст и пол ребенка при объяснении. Это очень важно."
                       "При объяснении учитывайте следующие аспекты, предоставленные родителем:"
                       "- Возраст и стадия развития ребенка")
        response = svc.chat_service.get_explainToChild(newPromt, systemPromt)
        content_text = response["content"]
    else:
        systemPromt = ("")
        response = svc.chat_service.get_explainToChild(prompt, systemPromt)
        content_text = response["content"] 
    return ChatResponse(response=content_text)

def decode_fairytale_response(content_text: str) -> FairytaleResponse:
    # Parse the JSON data to a Python dictionary
    data_dict = json.loads(content_text)

    # Extract the required fields from the data_dict
    titleOfTheFairyTale = data_dict.get("titleOfTheFairyTale", "")
    readingTime = data_dict.get("readingTime", "")
    contentOfTheFairyTale = data_dict.get("contentOfTheFairyTale", "")

    # Create a new dictionary with the extracted fields
    response_dict = {
        "titleOfTheFairyTale": titleOfTheFairyTale,
        "readingTime": readingTime,
        "contentOfTheFairyTale": contentOfTheFairyTale
    }

    # Create the FairytaleResponse object directly using the data
    fairytale_response = FairytaleResponse(**response_dict)

    return fairytale_response
