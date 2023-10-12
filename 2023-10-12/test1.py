import datetime

now = datetime.datetime.now()
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")
print("\n\n")
print(now.year, "년", now.month, "월", now.day, "일",
      now.hour, "시", now.minute, "분", now.second, "초")
print("\n\n")
print("{}년 {}월 {}일 {}시 {}분 {}초".format(now.year, now.month, now.day,
                                       now.hour, now.minute, now.second))
print("\n\n")
if 3 <= now.month <= 5:
    print("비번 달음 {}월로 분 입니다.".format(now.month))
if 6 <= now.month <= 8:
    print("비번 달음 {}월로 여름 입니다.".format(now.month))
if 9 <= now.month <= 11:
    print("비번 달음 {}월로 가을 입니다.".format(now.month))
if 12 <= now.month <= 2:
    print("비번 달음 {}월로 겨울 입니다.".format(now.month))
