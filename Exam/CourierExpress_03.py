packetWeight = float(input())
deliveryType = input()
overallKilometres = int(input())
price = 0

if deliveryType == "standard":
    if packetWeight < 1:
        price += 0.03 * overallKilometres
    elif 1 <= packetWeight < 10:
        price += 0.05 * overallKilometres
    elif 10 <= packetWeight < 40:
        price += 0.1 * overallKilometres
    elif 40 <= packetWeight < 90:
        price += 0.15 * overallKilometres
    elif 90 <= packetWeight < 150:
        price += 0.2 * overallKilometres

if deliveryType == "express":
    if packetWeight < 1:
        price += (0.03 * overallKilometres) + (0.8 * 0.03 * packetWeight) * overallKilometres
    elif 1 <= packetWeight < 10:
        price += (0.05 * overallKilometres) + (0.4 * 0.05 * packetWeight) * overallKilometres
    elif 10 <= packetWeight < 40:
        price += (0.1 * overallKilometres) + (0.05 * 0.1 * packetWeight) * overallKilometres
    elif 40 <= packetWeight < 90:
        price += 0.15 * overallKilometres + (0.02 * 0.15 * packetWeight) * overallKilometres
    elif 90 <= packetWeight < 150:
        price += 0.2 * overallKilometres + (0.01 * 0.20 * packetWeight) * overallKilometres

print("The delivery of your shipment with weight of {:.3f} kg. would cost {:.2f} lv.".format(packetWeight, price))
