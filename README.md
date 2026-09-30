# LLM을 활용한 Vibe Coding Level Up

OpenAI Responses API를 활용해 **LLM을 실제 서비스와 연결하는 기본
흐름**을 직접 실습하는 강의 자료입니다.

이 실습에서는 단순히 LLM에 질문하는 수준을 넘어, API를 이용해
**스트리밍, 대화 연속성, 구조화된 데이터, 음성 전사, Function
Calling**까지 단계적으로 경험합니다.

> **실습 흐름:** LLM 이해 → API 호출 → 스트리밍 → 대화 연속성 → 구조화된
> 데이터 → 음성 명령 → Function Calling → AI 에이전트 핵심 기술 이해

------------------------------------------------------------------------

## 1. 학습 목표

실습을 마치면 다음과 같은 흐름을 이해할 수 있습니다.

-   Python에서 OpenAI API를 호출하는 방법
-   Responses API의 기본 구조 이해
-   `instructions`, `input`, `response.output_text` 활용
-   웹 검색 도구를 API에 연결하는 방법
-   Streaming으로 생성 결과를 실시간 처리하는 방법
-   `previous_response_id`를 이용한 대화 연속성 구현
-   JSON Schema를 이용한 Structured Outputs 구현
-   음성 녹음 파일을 OpenAI 음성 전사(STT)로 변환
-   Function Calling을 이용해 LLM과 실제 프로그램의 기능을 연결
-   AI 에이전트를 구성하는 핵심 기술 요소 이해

------------------------------------------------------------------------

## 2. 실습 환경

노트북은 다음 환경을 기준으로 작성되었습니다.

-   Python 3.13.x
-   Jupyter Notebook
-   OpenAI Python SDK
-   `python-dotenv`
-   음성 실습: `numpy`, `scipy`, `sounddevice`

노트북 파일:

``` text
OpenAI_Responses_API.ipynb
```

------------------------------------------------------------------------

## 3. 사전 준비

### 3-1. Python 가상환경 생성

터미널에서 다음 명령을 실행합니다.

``` bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows 환경에서는 다음과 같이 활성화할 수 있습니다.

``` powershell
.venv\Scripts\activate
```

### 3-2. 기본 패키지 설치

``` bash
pip install openai python-dotenv
```

음성 녹음 실습까지 진행하는 경우:

``` bash
pip install numpy scipy sounddevice
```

------------------------------------------------------------------------

## 4. OpenAI API Key 설정

API Key는 소스코드에 직접 입력하지 않는 것을 권장합니다.

### 개인 PC에서 실행하는 경우

프로젝트 폴더에 `.env` 파일을 만들고 다음과 같이 저장합니다.

``` env
OPENAI_API_KEY=여기에_발급받은_API_KEY
```

Python에서는 `python-dotenv`를 이용해 환경변수를 불러옵니다.

``` python
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()
```

> API Key를 노트북 코드, GitHub 저장소, 출력 결과 등에 직접 입력하거나
> 커밋하지 마세요.

------------------------------------------------------------------------

## 5. GitHub Codespaces에서 API Key 사용

Codespaces에서는 API Key를 소스코드에 직접 넣는 대신 **GitHub Codespaces
Secrets**를 사용하는 방식을 실습합니다.

GitHub에서 다음 경로로 이동합니다.

``` text
GitHub → Settings → Codespaces → Secrets
```

Secret을 다음과 같이 등록합니다.

  항목                입력 내용
  ------------------- -----------------------------
  Name                `OPENAI_API_KEY`
  Value               OpenAI에서 발급받은 API Key
  Repository access   사용할 Repository

등록 후 Codespace에서 환경변수로 사용할 수 있습니다.

``` python
from openai import OpenAI

client = OpenAI()
```

------------------------------------------------------------------------

## 6. OpenAI 개발자 문서

API를 사용할 때는 공식 개발자 문서를 함께 확인하는 습관을 갖는 것이
중요합니다.

[OpenAI 개발자 문서](https://developers.openai.com/api/docs)

실습에서는 문서에서 필요한 API와 파라미터를 직접 찾아보는 것을
권장합니다.

------------------------------------------------------------------------

# 7. Responses API 기본 호출

가장 먼저 Responses API를 이용해 LLM을 호출합니다.

기본적인 구조는 다음과 같습니다.

``` python
from openai import OpenAI

client = OpenAI()

MODEL = "gpt-6-luna"

response = client.responses.create(
    model=MODEL,
    input="바이브코더의 고민에 대한 에세이 한문장을 작성해주세요",
)

print(response.output_text)
```

### 주요 요소

  요소                     역할
  ------------------------ ------------------------------
  `model`                  사용할 모델
  `instructions`           모델의 역할과 응답 규칙
  `input`                  사용자의 질문 또는 작업 지시
  `response.output_text`   모델이 생성한 텍스트
  `stream=True`            생성 결과를 순차적으로 받기
  `previous_response_id`   이전 응답과 다음 요청을 연결

> 사용하는 계정과 환경에서 이용 가능한 모델명으로 `MODEL` 값을
> 변경하세요.

------------------------------------------------------------------------

# 8. Web Search 활용

Responses API에는 도구를 연결할 수 있습니다.

노트북에서는 `web_search`를 이용해 최신 정보를 검색하는 실습을
진행합니다.

``` python
response = client.responses.create(
    model=MODEL,
    tools=[{"type": "web_search"}],
    input="오늘자 바이브코딩 관련한 뉴스를 한 가지 알려주세요.",
)

print(response.output_text)
```

이를 통해 다음과 같은 차이를 경험할 수 있습니다.

``` text
일반 LLM 호출
      ↓
모델이 알고 있는 정보 기반 응답

Web Search 연결
      ↓
외부 검색 도구 활용
      ↓
최신 정보 기반 응답
```

------------------------------------------------------------------------

# 9. Streaming

일반적인 API 호출은 응답이 완성된 후 결과를 받습니다.

Streaming을 사용하면 모델이 생성하는 결과를 순차적으로 받을 수 있습니다.

``` python
stream = client.responses.create(
    model=MODEL,
    instructions="당신은 파이썬 프로그래머입니다.",
    input="피보나치 수열을 생성하는 파이썬 프로그램을 작성해주세요.",
    stream=True,
)

final_answer = []

for event in stream:
    if event.type == "response.output_text.delta":
        final_answer.append(event.delta)
        print(event.delta, end="")

final_answer = "".join(final_answer)
```

### 핵심 개념

``` text
사용자 요청
    ↓
LLM 응답 생성
    ↓
delta
    ↓
delta
    ↓
delta
    ↓
화면에 실시간 출력
```

실제 AI 서비스의 채팅창에서 답변이 한 글자 또는 한 덩어리씩 나타나는
방식과 연결되는 개념입니다.

------------------------------------------------------------------------

# 10. 연쇄적인 대화

LLM 서비스에서는 이전 대화의 문맥을 다음 요청에 연결해야 하는 경우가
많습니다.

Responses API에서는 `previous_response_id`를 활용할 수 있습니다.

``` python
response = client.responses.create(
    model=MODEL,
    instructions="You are a helpful assistant. You must answer in Korean.",
    input="대한민국의 수도는 어디인가요?",
)

print(response.output_text)
```

다음 요청에서 이전 응답의 ID를 전달합니다.

``` python
second_response = client.responses.create(
    model=MODEL,
    instructions="You are a helpful assistant. You must answer in Korean.",
    input="이전 답변을 영어로 답변해 주세요.",
    previous_response_id=response.id,
)

print(second_response.output_text)
```

노트북에서는 이를 함수로 추상화해 반복적인 API 호출을 줄이는 방법도
실습합니다.

------------------------------------------------------------------------

# 11. Structured Outputs

LLM의 결과를 사람이 읽는 문장이 아니라 **프로그램에서 사용할 수 있는
구조화된 데이터**로 받고 싶을 때 Structured Outputs를 사용할 수
있습니다.

예를 들어 대한민국의 수도를 다음과 같은 JSON 구조로 받도록 지정할 수
있습니다.

``` json
{
  "capital": "서울특별시"
}
```

Python에서는 JSON Schema를 정의합니다.

``` python
capital_schema = {
    "type": "object",
    "properties": {
        "capital": {"type": "string"}
    },
    "required": ["capital"],
    "additionalProperties": False,
}
```

그리고 `text.format`에 schema를 지정합니다.

``` python
capital_response = client.responses.create(
    model=MODEL,
    input="대한민국의 수도는 어디인가요?",
    text={
        "format": {
            "type": "json_schema",
            "name": "country_capital",
            "strict": True,
            "schema": capital_schema,
        }
    },
)

print(capital_response.output_text)
```

------------------------------------------------------------------------

# 12. 구조화된 데이터로 퀴즈 만들기

Structured Outputs를 활용하면 단순 텍스트 생성에서 더 나아가 프로그램이
바로 사용할 수 있는 데이터를 생성할 수 있습니다.

실습에서는 통계 문제를 다음과 같은 구조로 생성합니다.

``` json
{
  "question": "...",
  "choices": ["...", "...", "...", "..."],
  "answer_index": 1,
  "difficulty": "하"
}
```

JSON Schema에서는 다음 필드를 정의합니다.

  필드             의미
  ---------------- ---------------
  `question`       문제
  `choices`        선택지
  `answer_index`   정답의 인덱스
  `difficulty`     문제 난이도

응답을 Python 객체로 변환하면 이후 웹 서비스나 프로그램에서 바로 활용할
수 있습니다.

``` python
import json

quiz_obj = json.loads(quiz_response.output_text)
```

### 핵심 포인트

``` text
LLM
 ↓
자연어 생성
 ↓
JSON Schema
 ↓
정해진 구조의 데이터
 ↓
Python 프로그램
 ↓
웹 서비스 / 업무 서비스
```

------------------------------------------------------------------------

# 13. 음성 명령과 STT

다음 단계에서는 텍스트 입력을 넘어 음성을 AI 서비스에 연결합니다.

실습 흐름은 다음과 같습니다.

``` text
마이크
 ↓
음성 녹음
 ↓
WAV 파일
 ↓
OpenAI 음성 전사
 ↓
텍스트 명령
```

필요한 패키지:

``` bash
pip install numpy scipy sounddevice
```

노트북에서는 다음과 같은 함수로 음성을 녹음합니다.

``` python
record_user_voice()
```

그리고 OpenAI의 음성 전사 기능을 이용합니다.

``` python
transcription = client.audio.transcriptions.create(
    model="gpt-transcribe",
    file=audio_file,
)
```

예제에서는 다음과 같은 음성 명령을 사용합니다.

``` text
냉장고 문 열어줘.
```

음성이 텍스트로 변환된 후 다음 단계의 Function Calling으로 전달됩니다.

------------------------------------------------------------------------

# 14. Function Calling

Function Calling은 LLM의 답변을 실제 프로그램의 **함수 실행**과 연결하는
핵심 기술입니다.

예제에서는 냉장고 문을 여는 함수를 정의합니다.

``` python
def open_refrigerator_door(door):
    return {
        "success": True,
        "door": door,
        "message": "냉장고 문을 열었습니다. (실습용 시뮬레이션)"
    }
```

LLM에는 사용할 수 있는 함수를 도구로 설명합니다.

``` text
사용자
 ↓
"냉장고 문 열어줘"
 ↓
LLM
 ↓
Function Call
 ↓
open_refrigerator_door()
 ↓
함수 실행 결과
 ↓
LLM
 ↓
최종 답변
```

실습에서는 실제 냉장고를 제어하는 것이 아니라 **함수 실행을
시뮬레이션**합니다.

------------------------------------------------------------------------

# 15. Function Calling의 전체 흐름

Responses API에서 Function Calling은 다음 순서로 진행됩니다.

### ① 사용자 명령

``` text
냉장고 문 열어줘.
```

### ② LLM이 함수 호출 결정

``` text
open_refrigerator_door
```

### ③ 함수 실행

``` python
result = open_refrigerator_door(**arguments)
```

### ④ 실행 결과를 LLM에 전달

``` python
{
    "type": "function_call_output",
    "call_id": item.call_id,
    "output": json.dumps(result, ensure_ascii=False),
}
```

### ⑤ LLM의 최종 답변

``` text
냉장고 문을 열었습니다.
```

즉, LLM이 직접 현실의 기능을 수행하는 것이 아니라,

> **LLM이 어떤 기능을 실행해야 하는지 판단하고 → 프로그램이 실제 함수를
> 실행하고 → 그 결과를 다시 LLM에게 전달하는 구조**

입니다.

------------------------------------------------------------------------

# 16. AI 에이전트 핵심 기술 4대 요소

실습 마지막에는 AI 에이전트를 구성하는 핵심 요소를 다음과 같이
정리합니다.

  ----------------------------------------------------------------------------
  기술 요소         핵심 개념         개발자 관점            사용자 관점
  ----------------- ----------------- ---------------------- -----------------
  **시스템          AI의 기본 성격과  응답 규칙과 역할 정의  전문적인 AI처럼
  프롬프트**        행동 규칙                                사용

  **Function        LLM과 외부 기능을 자연어를 함수 실행으로 "말했는데 실제로
  Calling**         연결하는          연결                   동작"
                    인터페이스                               

  **MCP**           외부 데이터와     다양한 데이터·도구     여러 서비스의
                    도구를 연결하는   연결                   정보를 AI가 활용
                    통합 표준                                

  **Harness         AI가 안전하게     자동화·격리·실행환경   안정성과 보안
  Engineering**     일할 수 있는      설계                   측면 개선
                    환경과 제어 설계                         
  ----------------------------------------------------------------------------

------------------------------------------------------------------------

# 17. 전체 실습 구조

이번 실습은 단순한 API 호출에서 출발해 점차 **AI 서비스 개발**의 형태로
확장됩니다.

``` text
LLM 기본 이해
      ↓
OpenAI Responses API
      ↓
기본 API 호출
      ↓
Web Search
      ↓
Streaming
      ↓
대화 연속성
      ↓
Structured Outputs
      ↓
음성 전사(STT)
      ↓
Function Calling
      ↓
AI Agent
```

핵심은 각각의 기술을 별도로 암기하는 것이 아니라,

> **LLM을 프로그램의 기능과 데이터에 연결하면 어떤 서비스가
> 만들어지는가?**

를 직접 경험하는 것입니다.

------------------------------------------------------------------------

# 18. 실습 파일

``` text
.
├── OpenAI_Responses_API.ipynb
└── README.md
```

### 실행 순서

1.  Python 환경 준비
2.  필요한 패키지 설치
3.  OpenAI API Key 설정
4.  Jupyter Notebook 실행
5.  `OpenAI_Responses_API.ipynb` 열기
6.  위에서부터 셀을 순서대로 실행
7.  각 단계의 코드를 직접 수정해 결과 비교
8.  마지막에는 자신의 업무에 적용할 수 있는 Function Calling 아이디어를
    생각해 보기

------------------------------------------------------------------------

# 19. 실습에서 직접 바꿔보기

강의에서는 예제 코드를 그대로 실행하는 것에서 끝내지 말고 다음과 같이
변경해 보는 것을 권장합니다.

### 기본 호출

``` text
"바이브코더의 고민에 대한 에세이"
```

를 다른 주제로 변경해 봅니다.

### Web Search

``` text
오늘자 바이브코딩 관련 뉴스
```

대신 자신이 관심 있는 최신 주제를 검색해 봅니다.

### Streaming

피보나치 프로그램 대신 자신이 원하는 프로그램을 생성해 봅니다.

### Structured Outputs

통계 퀴즈 대신 다음과 같은 구조를 생각해 볼 수 있습니다.

``` text
민원 분류
회의록 요약
보고서 정보 추출
업무 인수인계 데이터
공문 핵심정보 추출
```

### Function Calling

냉장고 제어 대신 자신의 업무에 필요한 함수를 설계해 봅니다.

``` text
날씨 조회
문서 검색
업무 담당자 조회
민원 분류
보고서 생성
통계 조회
```

------------------------------------------------------------------------

# 20. 중요한 보안 주의사항

API Key는 비밀번호와 같이 취급해야 합니다.

### 하지 말아야 할 것

``` text
❌ Python 코드에 API Key 직접 입력
❌ GitHub에 API Key 커밋
❌ 공개 README에 API Key 작성
❌ 출력 결과에 API Key 노출
❌ 다른 사람과 API Key 공유
```

### 권장 방식

``` text
개인 PC
→ .env / 환경변수

GitHub Codespaces
→ Codespaces Secrets
```

특히 GitHub 저장소가 공개되어 있다면 API Key가 포함되지 않았는지 반드시
확인합니다.

------------------------------------------------------------------------

## 21. 강의 핵심 메시지

이번 실습의 목표는 OpenAI API 문법을 외우는 것이 아닙니다.

**LLM을 하나의 대화형 도구로 사용하는 단계에서 벗어나, API를 통해
데이터와 기능을 연결하여 실제 서비스를 만드는 사고방식**을 익히는
것입니다.

``` text
LLM을 사용한다
        ↓
LLM을 API로 호출한다
        ↓
데이터를 연결한다
        ↓
도구를 연결한다
        ↓
함수를 실행한다
        ↓
업무 서비스로 확장한다
```

> **Vibe Coding의 다음 단계는 AI에게 코드를 맡기는 것이 아니라, AI가
> 실제로 일할 수 있는 구조를 설계하는 것입니다.**
