import random
import streamlit as st

def get_computer_choice():
    """
    컴퓨터의 선택을 무작위로 결정합니다.
    """
    return random.choice(['가위', '바위', '보'])

def determine_winner(user, computer):
    """
    사용자와 컴퓨터의 선택을 비교하여 승자를 결정합니다.
    """
    if user == computer:
        return "무승부!"
    elif (user == '가위' and computer == '보') or \
         (user == '바위' and computer == '가위') or \
         (user == '보' and computer == '바위'):
        return "사용자 승리!"
    else:
        return "컴퓨터 승리!"

def play_game():
    """
    스트림릿을 사용하여 게임을 실행하는 함수입니다.
    """
    st.title("가위바위보 게임")

    st.write("가위, 바위, 보 중 하나를 선택하세요:")
    user_choice = st.selectbox("선택하기", ["가위", "바위", "보"])

    if st.button("게임 시작"):
        computer_choice = get_computer_choice()
        st.write(f"사용자 선택: {user_choice}")
        st.write(f"컴퓨터 선택: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        st.write(f"결과: {result}")

if __name__ == "__main__":
    play_game()


# import random
# import streamlit as st

# def determine_winner(choices):
#     """
#     각 플레이어의 선택을 비교하여 승자를 결정합니다.
#     """
#     results = {'가위': 0, '바위': 0, '보': 0}

#     # 각 플레이어의 선택을 결과에 추가합니다.
#     for choice in choices:
#         results[choice] += 1

#     winners = []

#     # 승리 조건을 기반으로 코드 작성
#     if results['가위'] > 0 and results['보'] > 0 and results['바위'] == 0:
#         winners = ['가위']
#     elif results['바위'] > 0 and results['가위'] > 0 and results['보'] == 0:
#         winners = ['바위']
#     elif results['보'] > 0 and results['바위'] > 0 and results['가위'] == 0:
#         winners = ['보']

#     # 승자가 여러명인 경우
#     if len(winners) == 1:
#         win_condition = winners[0]
#         return [index for index, choice in enumerate(choices) if choice == win_condition]
#     else:
#         return []

# def play_game():
#     """
#     스트림릿을 사용하여 가위바위보 게임을 실행하는 함수입니다.
#     """
#     st.title("4인 가위바위보 게임")

#     players = [f"플레이어 {i+1}" for i in range(4)]
#     choices = []

#     for player in players:
#         choice = st.selectbox(f"{player} 선택:", ["가위", "바위", "보"], key=player)
#         choices.append(choice)

#     if st.button("결과 보기"):
#         st.write("### 선택 결과:")
#         for i, choice in enumerate(choices):
#             st.write(f"{players[i]} 선택: {choice}")

#         winners = determine_winner(choices)

#         if winners:
#             st.write("### 승자:")
#             for winner in winners:
#                 st.write(f"{players[winner]} 승리!")
#         else:
#             st.write("무승부입니다!")

# if __name__ == "__main__":
#     play_game()