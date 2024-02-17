priceTrip = float(input())
numPuzzles = int(input())
numTalkingDolls = int(input())
numTeddyBears = int(input())
numMinions = int(input())
numTrucks = int(input())

numOfToys = numPuzzles + numTalkingDolls + numTeddyBears + numMinions + numTrucks
sumPrice = numPuzzles * 2.60 + numTalkingDolls * 3 + numTeddyBears * 4.10 + numMinions * 8.20 + numTrucks * 2

discount = sumPrice * 0.25
priceWithDiscount = sumPrice - discount
rentWithDiscount = priceWithDiscount * 0.10
profitWithDiscount = priceWithDiscount - rentWithDiscount

noDiscountRent = sumPrice * 0.10
noDiscountProfit = sumPrice - noDiscountRent

remainingMoneyWithDiscount = profitWithDiscount - priceTrip
noDiscountRemainingMoney = priceTrip - noDiscountProfit

roundRMWD = '{:.2f}'.format(remainingMoneyWithDiscount)
roundND = '{:.2f}'.format(noDiscountRemainingMoney)

if numOfToys >= 50:
    print(f'Yes! {roundRMWD} USD left.')
else:
    print(f"Not enough money! {roundND} USD needed.")




