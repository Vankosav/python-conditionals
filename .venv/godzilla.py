movieBudget = float(input())
numExtras = int(input())
priceClothingOneExtra = float(input())

sumDecor = movieBudget * 0.10
sumClothes = numExtras * priceClothingOneExtra

if numExtras > 150:
    sumClothesWithDiscount = sumClothes * 0.90
    totalCost = sumDecor + sumClothesWithDiscount
else:
    totalCost = sumDecor + sumClothes

if totalCost > movieBudget:
    notEnough = totalCost - movieBudget
    print(f"Not enough money!\nWingard needs {notEnough:.2f} USD more.")
else:
    remaining = movieBudget - totalCost
    print(f"Action!\nWingard starts filming with {remaining:.2f} USD left.")
