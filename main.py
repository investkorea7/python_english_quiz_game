import json
import random

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

class QuizGame:
    def __init__(self, quizzes, best_score=0):
        self.quizzes = quizzes
        self.best_score = best_score

    def show_quiz_list(self):
        print()
        print("===== 퀴즈 목록 =====")

        for i, quiz in enumerate(self.quizzes, start=1):
            print(f"{i}. {quiz.question}")

        print(f"총 {len(self.quizzes)}개의 퀴즈가 있습니다.")

    def show_best_score(self):
        print(f"최고 점수: {self.best_score} / {len(self.quizzes)}")    

def save_state(quizzes, best_score):
    data = {
        "best_score": best_score,
        "quizzes": []
    }

    for quiz in quizzes:
        data["quizzes"].append({
            "question": quiz.question,
            "choices": quiz.choices,
            "answer": quiz.answer
        })

    with open("state.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def load_state():
    try:
        with open("state.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        loaded_quizzes = []

        for item in data["quizzes"]:
            loaded_quizzes.append(
                Quiz(
                    item["question"],
                    item["choices"],
                    item["answer"]
                )
            )

        loaded_best_score = data.get("best_score", 0)

        return loaded_quizzes, loaded_best_score

    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        return None, 0

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

loaded_quizzes, loaded_best_score = load_state()

if loaded_quizzes is not None:
    quizzes = loaded_quizzes
    best_score = loaded_best_score
else:
    best_score = 0

game = QuizGame(quizzes, best_score)

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
        score = 0

        print()
        print(f"퀴즈를 시작합니다! 총 {len(quizzes)}문제")
        print("-" * 40)

        shuffled_quizzes = quizzes.copy()
        random.shuffle(shuffled_quizzes)

        for quiz in shuffled_quizzes:
            quiz.show()

            while True:
                user_input = input("정답 번호를 입력하세요 (1-4): ").strip()

                if user_input == "":
                    print("입력값이 비어 있습니다. 다시 입력해주세요.")
                    continue

                try:
                    user_answer = int(user_input)
                except ValueError:
                    print("숫자만 입력해주세요.")
                    continue

                if user_answer < 1 or user_answer > 4:
                    print("1부터 4 사이의 숫자를 입력해주세요.")
                    continue

                break

            if quiz.check_answer(user_answer):
                print("정답입니다!")
                score += 1
            else:
                print("오답입니다.")

            print("-" * 40)

        print(f"결과: {len(quizzes)}문제 중 {score}문제 정답!")
        if score > best_score:
            best_score = score
            game.best_score = best_score
            save_state(quizzes, best_score)

    elif choice == "2":
        print()
        print("새로운 퀴즈를 추가합니다.")

        while True:
            question = input("문제를 입력하세요: ").strip()

            if question == "":
                print("문제는 비워둘 수 없습니다.")
                continue

            break

        choices = []

        for i in range(1, 5):
            while True:
                choice_text = input(f"선택지 {i}: ").strip()

                if choice_text == "":
                    print("선택지는 비워둘 수 없습니다.")
                    continue

                choices.append(choice_text)
                break

        while True:
            answer_input = input("정답 번호를 입력하세요 (1-4): ").strip()

            try:
                answer = int(answer_input)
            except ValueError:
                print("숫자만 입력해주세요.")
                continue

            if answer < 1 or answer > 4:
                print("1부터 4 사이의 숫자를 입력해주세요.")
                continue

            break

        new_quiz = Quiz(question, choices, answer)
        quizzes.append(new_quiz)

        save_state(quizzes, best_score)

        print("퀴즈가 추가되었습니다!")

    elif choice == "3":
        game.show_quiz_list()

    elif choice == "4":
        game.show_best_score()

    elif choice == "5":
        print("프로그램을 종료합니다.")
        break

    else:
        print("잘못된 입력입니다.")                