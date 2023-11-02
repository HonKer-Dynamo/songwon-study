for i in range(5):
    print("demo")

print("\n")

for character in "demo":
    print("-", character)

print("\n")

list_of_list = [[1, 2, 3], [4, 5, 6, 7], [8, 9]]
for items in list_of_list:
    print(items)

print("\n")

for items in list_of_list:
    for item in items:
        print(items)

print("\n")

a = [1, 2, 3, 4]
b = [*a, *a]
print(b)

print("\n")

numbers = [273, 103, 5, 32,  65, 9, 72, 800, 99]
for number in numbers:
    if number >= 100:
        print("- 100 이상의 수:", number)

print("\n")

for number in numbers:
    if number % 2 == 1:
        print(number, "는 홀수 입니다.")
    else:
        print(number, "는 짝수 입니다.")

print("\n")

