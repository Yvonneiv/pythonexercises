from math import pi
figureType = (input())
area = 0

if figureType == 'square':
    a = float(input())
    area = a * a

elif figureType == 'rectangle':
    a = float(input())
    b = float(input())
    area = a * b

elif figureType == 'circle':
    r = float(input())
    area = pi * (r ** 2)

elif figureType == 'triangle':
    a = float(input())
    b = float(input())
    area = 1 / 2 * a * b

print(area)

