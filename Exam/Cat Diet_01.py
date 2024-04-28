percentageOfFats = int(input())
percentageOfProteins = int(input())
percentageOfCarbs = int(input())
totalSumOfCalories = int(input())
percentageOfWater = int(input())

# 1 gram of fats = 9 calories
# 1 gram of proteins = 4 calories
# 1 gram of carbs = 4 calories

# 1) Calculating the fats in grams - % fats * totalSumOfCalories / 9 = sumOfFats
# 2) Calculating the proteins in grams - % proteins * totalSumOfCalories / 4  = sumOfProteins
# 3) Calculating the carbohydrates in grams - % carbs * totalSumOfCalories / 4 = sumOfCarbs
# 4) Calculating the total weight of the food - sumOfFats + sumOfProteins + sumOfCarbs = totalWeightOfFood
# 5) Calculating the calories for one gram = totalSumOfCalories/ totalWeightOfFood
# 6) Calculating the water percentage (100 - percentageOfWater)

sumOfFats = ((percentageOfFats / 100) * totalSumOfCalories) / 9
sumOfProteins = ((percentageOfProteins / 100) * totalSumOfCalories) / 4
sumOfCarbs = ((percentageOfCarbs / 100) * totalSumOfCalories) / 4
totalWeightOfFood = sumOfFats + sumOfProteins + sumOfCarbs
totalSumOfCaloriesPerGram = totalSumOfCalories / totalWeightOfFood
sumAfterCalculatingTheWater = ((100-percentageOfWater)/100) * totalSumOfCaloriesPerGram

print("{:.4f}".format(sumAfterCalculatingTheWater))
