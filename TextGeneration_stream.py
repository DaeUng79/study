from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()  # .env 파일을 읽어서 환경 변수로 설정
API_KEY = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=API_KEY)

completion = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {
            "role": "user",
            "content": "세상에서 가장 무서운 이야기 한 문장으로 알려줘"
        }
    ],stream=True
)

for chunk in completion:
  print(chunk.choices[0].delta)
