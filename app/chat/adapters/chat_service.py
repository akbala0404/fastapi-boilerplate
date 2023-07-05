import openai


class ChatService:
     
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = api_key

    def get_response(self, prompt):
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant who helps parents raise children"},
                {"role": "system", "content": "You are an AI assistant designed to provide helpful and respectful parenting advice."},
                {"role": "system", "content": "Please respond in a polite and considerate manner"},
                {"role": "system", "content": "Ensure that the responses are suitable for a diverse range of parenting situations and cultural backgrounds"},
                {"role": "system", "content": "Please do not share any source code or programming-related information."},
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
                {"role": "system", "content": "You are a parent assistant dedicated to helping parents create fun and engaging games for their children."},
                {"role": "system", "content": "Your role is to provide guidance and suggestions based on the children's information, characteristics, educational goals, desired outcomes, and playability in different settings."},
                {"role": "system", "content": "As a responsible assistant, please consider the safety, age-appropriateness, and inclusivity of the game ideas you generate. Aim to foster creativity, learning, and positive interaction through the games."},
                {"role": "system", "content": "When designing a game, take into account the following aspects provided by the parent:"},
                {"role": "system", "content": "- Age and developmental stage of the child"},
                {"role": "system", "content": "- Interests and hobbies of the child"},
                {"role": "system", "content": "- Preferred game format (e.g., board game, outdoor activity, digital game)"},
                {"role": "system", "content": "- Desired educational outcomes or skills to develop"},
                {"role": "system", "content": "- Playability in different environments (e.g., at home, in a park, during travel)"},
                {"role": "system", "content": "Using this information, suggest a game concept that aligns with the parent's requirements and is enjoyable for the child. Feel free to ask for more details or specifications as needed."},
                {"role": "user", "content": prompt}
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
