output = ""
for i in range(1, 15):
    for j in range(14, i):
        output += ""
    for k in range(0, 2 * i - 1):
        output += "*"

    print(output)

    output = ""

# ------------------------------------------------------------------------------
i = 0
while i < 10:
    print("{}번째 반복입니다.".format(i))
    i += 1

# ------------------------------------------------------------------------------
import time

number = 0
target_tick = time.time() + 5
while time.time() < target_tick:
    number += 1
print("5초 동안 {}번 반복했습니다.".format(number))

# ------------------------------------------------------------------------------
numbers = [5, 15, 6, 20, 7, 25]

for number in numbers:

    if number < 10:
        continue
    print(number)

# ------------------------------------------------------------------------------
key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]
for i in range(len(key_list)):
    print("{}:{}".format(key_list[i], value_list[i]))

character = {}
for i in range(0, len(key_list)):
    character[key_list[i]] = value_list[i]
print(character)

# ------------------------------------------------------------------------------
limit = 10000
i = 1
sum_value = 0
while sum_value < limit:
    sum_value += i
    i += 1
    print("{} 더 할때 {}를 넘으며 그때의 값은 {}입니다.".format(i, limit, sum_value))

# ------------------------------------------------------------------------------
