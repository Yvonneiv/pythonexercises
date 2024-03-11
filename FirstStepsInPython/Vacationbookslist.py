pens_price = 5.80
markers_price= 7.20
cleaning_detergent_per_liter_price=1.20

pens_count = int(input())
markers_count = int(input())
cleaning_detergent_litres=int(input())
percentage_discount =int(input())

total_sum_without_discount = (pens_count * pens_price) + (markers_count* markers_price) + (cleaning_detergent_litres * cleaning_detergent_per_liter_price)
percentage_discount = percentage_discount / 100
total_sum_with_discount = total_sum_without_discount - (total_sum_without_discount * percentage_discount)

print(total_sum_with_discount)
