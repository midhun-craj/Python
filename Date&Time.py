import datetime

# date = datetime.date(2025, 12, 24)
# print(date)

# today = datetime.date.today()
# print(today)

# time = datetime.time(13, 15, 1)
# print(time)

now = datetime.datetime.now()
# print(now)

now = now.strftime("%H:%M:%S %y-%m-%d")
print(now)