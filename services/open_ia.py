###############################################
#           Template made by HenriHTTP        #
#          https://github.com/HenriHTTP       #
#           Copyright© HenriHTTP, 2024        #
###############################################

from dotenv import load_dotenv
import os
import openai

load_dotenv()
OPEN_IA_TOKEN = os.getenv('OPEN_IA_TOKEN')
openai.api_key = OPEN_IA_TOKEN


class OpenAi:

    @staticmethod
    async def ask_gpt(messages):
        try:
            response = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": messages},
                ],
                temperature=0.7,
                max_tokens=150
            )
            return response['choices'][0]['message']['content']
        except Exception as error:
            print(f"Error asking GPT-3: {error}")
            return "An error occurred while processing your request."
