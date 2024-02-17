#sum seconds
import math

timeFirst = "{:02d}".format(int(input()))
timeSecond = "{:02d}".format(int(input()))
timeThird = "{:02d}".format(int(input()))

totalTime = int(timeFirst) + int(timeSecond) + int(timeThird)


minutes = math.floor(totalTime // 60)
seconds = totalTime % 60

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')