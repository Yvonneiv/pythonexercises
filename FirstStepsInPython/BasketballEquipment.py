annual_fee_for_basketball_practice = int(input())

basketball_sneakers_price = annual_fee_for_basketball_practice * 0.60
basketball_equipment_price = basketball_sneakers_price * 0.80
basketball_ball_price = basketball_equipment_price / 4
basketball_accessories = basketball_ball_price / 5

final_price = annual_fee_for_basketball_practice + basketball_sneakers_price + basketball_equipment_price + basketball_ball_price + basketball_accessories
print(final_price)