from os import getcwd
import math
from statistics import mean

with open(file= getcwd() + "\\advent_of_code\\input7.txt") as f:
    data = f.read().strip().split(sep=",")

"""Part One"""
def fuelConsumption1(value: int, fuelDict: dict):
    fuel = 0
    
    for key in fuelDict:
        if key != value:
            fuel += abs(key - value) * fuelDict[key]
    
    return fuel

"""Part two"""
def fuelConsumption2(value: int, fuelDict: dict):
    fuel = 0
    
    for key in fuelDict:
        if key != value:
            horizontalMovement = abs(key - value) 

            # formula for consecutive number adding
            # (stop - start + 1)/2 * (start + stop)
            # start == 1 always
            # stop / 2 * (1 + stop)
            fuel += int((horizontalMovement / 2) * (1 + horizontalMovement) * fuelDict[key])
                 

    return fuel

data = [int(x) for x in data]
minimum = min(data)
maximum = max(data)

fuelDict = {x : data.count(x) for x in range(minimum, maximum + 1)}

# change the fuelConsumption method
fuelConsumptions = {num : fuelConsumption2(num, fuelDict) for num in fuelDict}

least = math.inf
for key in fuelConsumptions:
    if fuelConsumptions[key] < least:
        least = fuelConsumptions[key]

print(least)

