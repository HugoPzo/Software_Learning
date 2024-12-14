import datetime

date = datetime.date(2026, 10, 2)
today = datetime.date.today()

time = datetime.time(15, 39,21)
now = datetime.datetime.now()

print(date)
print(today)

print(time)
now = now.strftime("%H:%M:%S - %d/%m/%Y")
print(now)


target_datetime = datetime.datetime(2030, 1, 2, 12, 30, 3)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has NOT passed")
