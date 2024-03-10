square_meters = float(input())
total_sum_without_discount = square_meters * 7.61
total_sum_with_discount = total_sum_without_discount * 0.82
discount_price = total_sum_without_discount - total_sum_with_discount

print(f'The final price is: {total_sum_with_discount:2f} lv.')
print(f'The discount is: {discount_price:2f} lv.')