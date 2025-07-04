import asyncio
from openai import AsyncOpenAI
from openai.helpers import LocalAudioPlayer
from dotenv import load_dotenv
import os

load_dotenv()  # .env 파일을 읽어서 환경 변수로 설정
API_KEY = os.getenv('OPENAI_API_KEY')

openai = AsyncOpenAI(api_key=API_KEY)

async def main() -> None:
    async with openai.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="shimmer",
        input="인공지능 개발에 흥미가 생기셨나요? 오늘을 시작으로 인공지능의 세계에 발을 들여보세요!",
        instructions="한국어로 말해주세요. 목소리는 부드럽고 친근하게, 그리고 약간의 감정을 담아주세요.",
        response_format="pcm",
    ) as response:
        await LocalAudioPlayer().play(response)

if __name__ == "__main__":
    asyncio.run(main())