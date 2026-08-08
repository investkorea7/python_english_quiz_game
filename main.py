class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def show(self):
        print(self.question)

        for i, choice in enumerate(self.choices, start=1):
            print(f"{i}. {choice}")

    def check_answer(self, user_answer):
        return user_answer == self.answer

quizzes = [
    Quiz(
        "abundant의 뜻은?",
        ["풍부한", "불안한", "정확한", "평범한"],
        1
    ),
    Quiz(
        "reluctant의 뜻은?",
        ["열정적인", "꺼리는", "친절한", "신중한"],
        2
    ),
    Quiz(
        "inevitable의 뜻은?",
        ["피할 수 없는", "예상 밖의", "일시적인", "의심스러운"],
        1
    ),
    Quiz(
        "contribute의 뜻은?",
        ["경쟁하다", "기여하다", "비교하다", "거절하다"],
        2
    ),
    Quiz(
        "significant의 뜻은?",
        ["사소한", "우연한", "중요한", "복잡한"],
        3
    )
]

while True:
    print("=" * 40)
    print("Python English Quiz Game")
    print("=" * 40)
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("=" * 40)

    choice = input("선택: ")

    if choice == "1":
        print("퀴즈 풀기를 선택하셨습니다.")

    elif choice == "2":
        print("퀴즈 추가를 선택하셨습니다.")

    elif choice == "3":
        print("퀴즈 목록을 선택하셨습니다.")

    elif choice == "4":
        print("점수 확인을 선택하셨습니다.")

    elif choice == "5":
        print("프로그램을 종료합니다.")
        break

    else:
        print("잘못된 입력입니다.")