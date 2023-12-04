# 함수를 건어
def fact(n):
    output = 1
    for i in range(1, n + 1):
        output *= i
    return output


# 함수호출하기
print("1!:", fact(1))
print("2!:", fact(2))
print("3!:", fact(3))
print("4!:", fact(4))
print("5!:", fact(5))
print("\nCircular Printing:")
for i in range(1, 6):
    print(f"{i}!:", fact(i))

print("-----------------------------------------------------------------------")


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


print("1!:", fact(1))
print("2!:", fact(2))
print("3!:", fact(3))
print("4!:", fact(4))
print("5!:", fact(5))

print("-----------------------------------------------------------------------")
