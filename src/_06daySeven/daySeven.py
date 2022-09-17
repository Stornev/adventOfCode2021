from makeLink import makeInputLink
import math

def getData():
    with open(file=makeInputLink(7)) as f:
        data = f.read().strip().split(sep=",")

    return data

def makeFuelDict(data: list):
    data = [int(x) for x in data]
    minimum = min(data)
    maximum = max(data)

    fuelDict = {x : data.count(x) for x in range(minimum, maximum + 1)}
    return fuelDict

def findLeast(fuelConsumptions: dict):
    least = math.inf
    for key in fuelConsumptions:
        if fuelConsumptions[key] < least:
            least = fuelConsumptions[key]

    return least

def fuelConsumption1(value: int, fuelDict: dict):
    fuel = 0
    
    for key in fuelDict:
        if key != value:
            fuel += abs(key - value) * fuelDict[key]
    
    return fuel

def partOne(data: list):
    fuelDict = makeFuelDict(data)
    fuelConsumptions = {num : fuelConsumption1(num, fuelDict) for num in fuelDict}
    return findLeast(fuelConsumptions)


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

def partTwo(data: list):
    fuelDict = makeFuelDict(data)
    fuelConsumptions = {num : fuelConsumption2(num, fuelDict) for num in fuelDict}
    return findLeast(fuelConsumptions)