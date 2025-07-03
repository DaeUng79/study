from openai import OpenAI
import base64
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=API_KEY)

prompt = """
건물의 오른쪽 위 글자는 "양산시청", 좌측 글자는 "소통과 공정 다시뛰는 양산"글자는 유지해야 합니다.
"을지훈련"이라는 문구와 함께, 건물이 파손되는 등 재난 상황을 사실적으로 그려줘
"""

result = client.images.edit(
    model="gpt-image-1",
    image=[
        open("yscity.jpg", "rb"),
    ],
    prompt=prompt,
    size="1536x1024",
)

image_base64 = result.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

# Save the image to a file
with open("image_edit6.png", "wb") as f:
    f.write(image_bytes)