print(len("안녕하세요"))
print("-------------------------------------------------------------------")


def print_n_times(value, n):
    for i in range(n):
        print(value)


print_n_times("안녕하세요", 5)
print("-------------------------------------------------------------------")


def print_n_times(n, *values):
    # n번 반복합니다.
    for i in range(n):
        # values 리스트처럼 활용합니다.
        for value in values:
            print(value)
        # 단순한 줄바꿈
        print()


# 함수를 호출합니다.
print_n_times(3, "안녕하세요", "즐거운", "파이썬 프로그래밍")

print("-------------------------------------------------------------------")


def test(a, b=10, c=100):
    print(a + b + c)


test(10, 20, 30)
test(a=10, b=100, c=200)
test(c=10, a=100, b=200)
test(9, c=200)
print("-------------------------------------------------------------------")


def return_test():
    print("A 위치입니다.")
    return
    print("B 위치입니다.")


return_test()
print("-------------------------------------------------------------------")


def return_test():
    return


value = return_test()
print(value)
print("-------------------------------------------------------------------")
