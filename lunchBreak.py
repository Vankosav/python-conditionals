import math


nameSeries = input()
episodeDuration = int(input())
breakDuration = int(input())


timeLunch = math.ceil(breakDuration * 0.125)
breakTime = math.ceil(breakDuration * 0.25)
remainingTime = breakDuration - timeLunch - breakTime
timeLeft = remainingTime - episodeDuration
neededTime = math.ceil(episodeDuration - remainingTime)


if remainingTime >= episodeDuration:
    print(f"You have enough time to watch {nameSeries} and left with {timeLeft} minutes free time.")
else:
    print(f"You don't have enough time to watch {nameSeries}, you need {neededTime} more minutes.")
