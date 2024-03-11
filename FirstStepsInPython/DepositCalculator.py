deposited_sum = float(input())
deposit_time = int(input())
annual_interest_rate = float(input())
accured_interest_rate = deposited_sum * (annual_interest_rate/100)
monthly_interest_rate = accured_interest_rate / 12
total_sum = deposited_sum + monthly_interest_rate * deposit_time
print(total_sum)
