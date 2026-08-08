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