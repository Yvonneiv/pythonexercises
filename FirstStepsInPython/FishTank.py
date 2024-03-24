length = int(input())
width = int(input())
height = int(input())
percentage = float(input())

volume = length * width * height
volume_in_litres = volume * 0.001
percentage_of_occupied_space = percentage / 100
needed_litres = volume_in_litres * (1-percentage_of_occupied_space)
print(needed_litres)