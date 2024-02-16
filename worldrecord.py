recordSec = float(input())
distanceMet = float(input())
timeSecForMeter = float(input())

mustSwim = distanceMet * timeSecForMeter
addingSeconds = (distanceMet // 15) * 12.5
totalTime = mustSwim + addingSeconds
roundTotalTime = '{:.2f}'.format(totalTime)

if recordSec < totalTime:
    neededSec = totalTime - recordSec
    roundNeededSec = '{:.2f}'.format(neededSec)
    print(f"No, he failed! He was {roundNeededSec} seconds slower.")
else:
    print(f'Yes, he succeeded! The new world record is {roundTotalTime} seconds.')