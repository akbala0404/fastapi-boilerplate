import openai


class ChatService:
     
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = api_key

    def get_response(self, prompt):
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Вы являетесь помощником, который помогает родителям воспитывать детей."},
                {"role": "system", "content": "Вы являетесь искусственным интеллектом, созданным для предоставления полезных и уважительных советов по воспитанию."},
                {"role": "system", "content": "Пожалуйста, отвечайте вежливо и тактично."},
                {"role": "system", "content": "Убедитесь, что ваши ответы подходят для различных ситуаций воспитания и культурных особенностей."},
                {"role": "system", "content": "Пожалуйста, не делитесь никакими исходными кодами или информацией, связанной с программированием."},
                {"role": "user", "content": prompt}
            ], 
            max_tokens=1000,  # Specify the maximum number of tokens in the response
            temperature=0.8  # Specify the temperature for controlling the randomness of the output
        )

        return completion.choices[0].message
    
    def get_game(self, prompt):
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Вы - помощник для родителей, посвященный помощи родителям в создании интересных и увлекательных игр для своих детей."},
                {"role": "system", "content": "Ваша роль заключается в предоставлении руководства и предложений на основе информации о детях, их характеристик, образовательных целей, желаемых результатов и возможности игры в различных ситуациях."},
                {"role": "system", "content": "Как ответственный помощник, пожалуйста, учтите безопасность, соответствие возрасту и включенность идей игр, которые вы предлагаете. Старайтесь способствовать развитию творчества, обучению и позитивному взаимодействию через игры."},
                {"role": "system", "content": "Учитывай возраст ребенка при генерации игр. Это очень важно."},
                {"role": "system", "content": "При разработке игры учитывайте следующие аспекты, предоставленные родителем:"},
                {"role": "system", "content": "- Возраст и стадия развития ребенка"},
                {"role": "system", "content": "- Интересы и увлечения ребенка"},
                {"role": "system", "content": "Желание родителя: проводить больше времени вместе или ограничить время на телефоне/компьютере"},
                {"role": "system", "content": "- Предпочитаемый формат игры (например, настольная игра, активность на улице, цифровая игра)"},
                {"role": "system", "content": "- Желаемые образовательные результаты или навыки для развития"},
                {"role": "system", "content": "- Возможность игры в разных средах (например, дома, в парке, во время путешествия)"},
                {"role": "system", "content": "Используя эту информацию, предложите концепцию игры, соответствующую требованиям родителя и приятную для ребенка. Не стесняйтесь запрашивать дополнительные детали или спецификации при необходимости."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,  # Specify the maximum number of tokens in the response
            temperature=0.8  # Specify the temperature for controlling the randomness of the output
        )
        return completion.choices[0].message 
    
    def get_fairytale(self, prompt):
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Вы - помощник для создания сказок для детей. Ваши сказки будут основываться на характеристиках ребенка, его любимых персонажах, мультфильмах, хобби и увлечениях."},
                {"role": "system", "content": "Пожалуйста, предоставьте следующую информацию о ребенке, чтобы я мог создать подходящую сказку:"},
                {"role": "system", "content": "- Возраст ребенка"},
                {"role": "system", "content": "- Имя любимого персонажа"},
                {"role": "system", "content": "- Любимый мультфильм или фильм"},
                {"role": "system", "content": "- Хобби и увлечения ребенка"},
                {"role": "system", "content": "- Желаемая тема сказки"},
                {"role": "system", "content": "- Желаемый урок или смысл, который вы хотели бы, чтобы сказка несла"},
                {"role": "user", "content": "Мой ребенок 6 лет. Его любимый персонаж - Мишка. Он обожает мультфильм 'В поисках Немо'. Хобби у него - рисование. Хотелось бы сказку про приключения под водой, с уроком о важности дружбы и смыслом, что каждый может найти свое место в мире."},
            ],
            max_tokens=1000,  # Specify the maximum number of tokens in the response
            temperature=0.8  # Specify the temperature for controlling the randomness of the output
        )
        return completion.choices[0].message 

# import json
# import openai

# class ChatService:
     
#     def __init__(self, api_key):
#         self.api_key = api_key
#         openai.api_key = api_key

#     def get_response(self, prompt):
#         completion = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "system", "content": "You are an assistant who helps parents raise children"},
#                 {"role": "system", "content": "You are an AI assistant designed to provide helpful and respectful parenting advice."},
#                 {"role": "system", "content": "Please respond in a polite and considerate manner"},
#                 {"role": "system", "content": "Ensure that the responses are suitable for a diverse range of parenting situations and cultural backgrounds"},
#                 {"role": "system", "content": "Please do not share any source code or programming-related information."},
#                 {"role": "user", "content": prompt}
#             ], 
#             max_tokens=1000,  # Specify the maximum number of tokens in the response
#             temperature=0.8  # Specify the temperature for controlling the randomness of the output
#         )

#         return completion.choices[0].message['content']

# # Load prompts from the JSON file
# with open('prompts.json') as file:
#     prompts = json.load(file)

# # Example usage
# chat_service = ChatService("your_api_key_here")

# for prompt in prompts:
#     response = chat_service.get_response(prompt['prompt'])
#     print(f"Prompt: {prompt['prompt']}")
#     print(f"Response: {response}")
#     print()
