budget = float(input())
numVideoCards = int(input())
numCPU = int(input())
numRam = int(input())


costVideoCards = numVideoCards * 250
costCPU = numCPU * (costVideoCards * 0.35)
costRAM = numRam * (costVideoCards * 0.10)


totalCost = costVideoCards + costCPU + costRAM


if numVideoCards > numCPU:

    discount = totalCost * 0.15
    totalCost -= discount


budgetLeft = budget - totalCost


if budgetLeft >= 0:
    print(f'You have {budgetLeft:.2f} USD left!')
else:
    budgetNeeded = abs(budgetLeft)
    print(f'Not enough money! You need {budgetNeeded:.2f} USD more!')



