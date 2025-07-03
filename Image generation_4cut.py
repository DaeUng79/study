
from openai import OpenAI
import base64
from dotenv import load_dotenv
import os

# .env 파일을 읽어서 환경 변수로 설정
load_dotenv()
API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=API_KEY)

prompt = """
4컷 만화을 사실적으로 생성합니다. 주제는 '치리의 올바른 칫솔질'입니다. 각 컷은 다음과 같은 내용을 포함합니다

헤드라인 "치리의 올바른 칫솔질" 문구를 포함합니다.

밝고 귀여운 유치원 교실 배경에서, 웃고 있는 어린 캐릭터 '치리'가 칫솔과 치약을 준비하고 있습니다. 치리는 다양한 색상의 칫솔을 들고 있으며, '치카치카 준비' 문구를 표시합니다.배경에는 칫솔과 치약이 정리된 선반이 보입니다. 밝은 색감과 친근한 분위기로 아이들의 관심을 끌 수 있도록 설정합니다.

치리가 큰 모션으로 칫솔질을 시작하는 장면. 치아 모형 앞에서 칫솔을 움직이며 웃고 있습니다. 치아 모형에는 깨끗해지는 과정을 보여주는 간단한 그래픽 효과가 추가되어 있습니다. 배경은 밝은 욕실로 설정하고, 치리의 표정은 즐겁고 신나 보이도합니다. 

치리가 칫솔을 위아래로 움직이며 모든 면을 꼼꼼히 닦고 있는 장면. 옆에는 '앞니, 어금니, 혀도 닦아요!'라는 간단한 문구가 함께 표시됩니다. 치리의 행동을 따라 배우는 아이들을 위해 칫솔의 움직임이 강조된 그래픽. 배경은 깨끗한 욕실 내부로 유지.

양치가 끝난 후 반짝이는 미소를 지으며 치리를 칭찬하는 유치원 선생님과 함께 행복해하는 장면. '아 상쾌해' 문구를 표시합니다. 치리 주변에는 반짝이는 별과 하트 같은 귀여운 그래픽 요소들이 추가되어 즐거운 분위기를 연출합니다. 배경은 밝고 따뜻한 교실이나 욕실로 설정.
"""


result = client.images.generate(
    model="gpt-image-1",
    prompt=prompt,
    quality="high",
    size="1024x1536",
)

image_base64 = result.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

# Save the image to a file
with open("4cut.png", "wb") as f:
    f.write(image_bytes)