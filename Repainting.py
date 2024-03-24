nylon = int(input())
liters_paint = int(input())
liters_thinner = int(input())
hours_work = int(input())

nylon_price_per_square_meter = 1.50
price_paint_per_liter = 14.50
price_thinner_per_liter = 5.00
price_plastic_bags = 0.40

total_sum_for_materials = ((nylon+2) * nylon_price_per_square_meter) + ((liters_paint * 1.1) * price_paint_per_liter) + (liters_thinner * price_thinner_per_liter) + price_plastic_bags
salary_for_one_hour_work = total_sum_for_materials * 0.30
total_sum_for_salaries = salary_for_one_hour_work * hours_work
final_sum = total_sum_for_materials + total_sum_for_salaries
print(final_sum)



