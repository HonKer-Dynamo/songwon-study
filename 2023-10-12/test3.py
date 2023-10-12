numbers = input("정수입력:")
last_character = numbers[-1]
last_number = int(last_character)
if last_number % 2 == 0:
    print("짝수입니다.")
if last_number % 2 == 1:
    print("홀수입니다.")
