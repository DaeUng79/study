
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# .env 파일을 읽어서 환경 변수로 설정
load_dotenv()
API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=API_KEY)

# Streamlit 애플리케이션 인터페이스
st.title("Story 생성기")
st.write("OpenAI의 GPT 모델을 사용하여 입력한 내용을 기반으로 이야기를 생성합니다.")

# 사용자 입력
user_input = st.text_input("이야기의 시작을 입력하세요:", "")

# 사용자 입력 처리 및 API 호출
if st.button("이야기 생성") and user_input:
    with st.spinner("이야기 생성 중..."):
        # OpenAI API 호출
        completion = client.chat.completions.create(
            model="gpt-4.1",
            messages=[
                {
                    "role": "user", "content": user_input
                }
            ],stream=True
        )

        # 결과 출력
        st.write_stream(completion)