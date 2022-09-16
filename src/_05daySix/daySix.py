from os import getcwd

with open(file= getcwd() + "\\src\\(daySix\\input6.txt") as f:
    data = f.read().strip().split(sep=",")

data = [int(x) for x in data]

"""Part One"""
# for i in range(80):
#     for x in range(len(data)):
#         current = data[x]

#         if current == 0:
#             data.append(8)
#             data[x] = 6
#         else:
#             data[x] -= 1

# print(len(data))

"""Part Two"""

# not 1619067452340
# between 1,619,067,452,340 - 2,000,000,000,000
# is 1,740,449,478,328 dictionaries FTW

def mainLoop(lanternFish: dict):

    for i in range(0, 10):
        temp = lanternFish[i]
        lanternFish[i-1] = temp

    zeroes = lanternFish[-1]
    lanternFish[6] += zeroes
    lanternFish[8] += zeroes

    lanternFish[-1] = 0


lanternFish = {i : 0 for i in range(-1,10)}
data.sort()


for i in range(len(data)):
    if data[i] in lanternFish:
        lanternFish[data[i]] += 1
    else:
        lanternFish[data[i]] = 0

for i in range(0,256):
    mainLoop(lanternFish)


total = 0
for key in lanternFish:
    total += lanternFish[key] 

print(total)
