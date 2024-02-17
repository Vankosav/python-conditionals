hour = int(input())
minutes = int(input())

minutes += 15
hour += minutes // 60
minutes %= 60
hour %= 24


if hour < 10:
    hour_str = str(hour)
else:
    hour_str = str(hour).zfill(2)

minutes_str = str(minutes).zfill(2)

print(f"{hour_str}:{minutes_str}")

