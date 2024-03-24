chicken_menus_count = int(input())
fish_menus_count = int(input())
veggie_menus_count = int(input())

price_per_one_chicken_menu = 10.35
price_per_one_fish_menu = 12.40
price_per_one_veggie_menu = 8.15
price_for_the_delivery_services = 2.50

total_price_for_menus = chicken_menus_count * price_per_one_chicken_menu + fish_menus_count * price_per_one_fish_menu +veggie_menus_count * price_per_one_veggie_menu
price_for_the_dessert = total_price_for_menus * 0.20
final_sum = total_price_for_menus + price_for_the_dessert + price_for_the_delivery_services
print(final_sum)