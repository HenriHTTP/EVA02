from dotenv import load_dotenv
import os
import openai
from discord.ext import commands

load_dotenv()
OPEN_IA_TOKEN = os.getenv('OPEN_IA_TOKEN')

openai.api_key = OPEN_IA_TOKEN


class OpenAi:

    @staticmethod
    async def ask_gpt(messages):
        try:
            response = openai.ChatCompletion.create(
                model='gpt-3.5-turbo-1',
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": messages},
                ],
                temperature=0.7,
                max_tokens=150
            )
            return response['choices'][0]['message']['content']
        except Exception as e:
            print(f"Error asking GPT-3: {e}")
            return "An error occurred while processing your request."
