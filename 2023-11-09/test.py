dict_a = {"name": "이변재스 겜스", "type": "히허로 무비"}
print(dict_a["name"])
# ------------------------------------------------------------------------------#
dictionary = {"name": "7D 건조 망고",
              "type": "당절임",
              "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
              "origin": "필리핀"
              }
value = dictionary.get("존재하지 않는 키")
print("값:", value)
for key in dictionary:
    print(key, ":", dictionary[key])

# -----------------------------------------------------------------------------#
pets = [
    {"name": "구름", "age": 5},
    {"name": "아지", "age": 3},
    {"name": "호랑이", "age": 1},
    {"name": "고양이", "age": 1}
]
for pet in pets:
    print(pet['name'], str(pet['age']) + '살')

# -----------------------------------------------------------------------------#
a = range(0, 5)
print(list(a))
b = range(5, 10)
print(list(b))
c = range(0, 10, 2)
print(list(c))
d = range(0, 10 + 1)
print(list(d))
n = 10
e = range(0, n // 2)
print(list(e))
for i in range(5):
    print(str(i) + "= 반복 변수")
print()
for i in range(5, 10):
    print(str(i) + "= 반복 변수")
print()
for i in range(0, 10, 3):
    print(str(i) + "= 반복 변수")
print()
# -----------------------------------------------------------------------------#
array = [273, 32, 103, 57, 52]
for i in range(len(array)):
    print("{}번째 반복: {}".format(i, array[i]))
print()
#  ----------------------------------------------------------------------------#
output = ""
for i in range(1,10):
    for j in range(0, i):
        output += "*"
    output += "\n"
print(output)
