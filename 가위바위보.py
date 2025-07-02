import random

def get_user_choice():
    """
    사용자로부터 가위, 바위, 보 중 하나를 입력받습니다.
    유효한 입력이 아닐 경우 다시 입력을 요청합니다.
    """
    choices = ['가위', '바위', '보']
    while True:
        user_input = input("가위, 바위, 보 중 하나를 선택하세요: ")
        if user_input in choices:
            return user_input
        else:
            print("잘못된 입력입니다. 다시 시도해주세요.")

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
    게임을 실행하는 메인 함수입니다.
    """
    print("=== 가위바위보 게임 ===")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"사용자 선택: {user_choice}")
    print(f"컴퓨터 선택: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(f"결과: {result}")

if __name__ == "__main__":
    while True:
        play_game()
        play_again = input("다시 하시겠습니까? (y/n): ")
        if play_again.lower() != 'y':
            print("게임을 종료합니다. 감사합니다!")
            break