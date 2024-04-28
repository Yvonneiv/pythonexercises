pocketMoneyOfTeresaPerDay = float(input())
moneyGainedPerDay = float(input())
expensesForTheWholePeriod = float(input())
neededMoneyForThePresent = float(input())


savingsFromThePocketMoney = 5 * pocketMoneyOfTeresaPerDay
moneyGained = 5 * moneyGainedPerDay
totalSumOfGainedMoney = savingsFromThePocketMoney + moneyGained
totalSumOfMoneyAfterTheExpenses = totalSumOfGainedMoney - expensesForTheWholePeriod

if (totalSumOfMoneyAfterTheExpenses>=neededMoneyForThePresent):
 print("Profit: {:.2f} BGN, the gift has been purchased.".format(totalSumOfMoneyAfterTheExpenses))
else:
  print("Insufficient money: {:.2f} BGN.".format(neededMoneyForThePresent - totalSumOfMoneyAfterTheExpenses))

