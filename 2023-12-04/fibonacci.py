# 번수를 선어합니다
counter = 0
# 함수를 선언합니다
def fiboncci(n):
    # 어떤 피보나치 수를 구하는지 출력합니다
    print("fiboncci({})를 구합니다.".format(n))
    global counter
    counter += 1
    # 피보나치 수를 구합니다
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fiboncci(n - 1) + fiboncci(n - 2)
#  함수를 호출합니다
fiboncci(35)
print("----")
print("fiboncci(10) 함수를 호출한 횟수: ", counter)