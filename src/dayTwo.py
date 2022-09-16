import os

with open(file= os.getcwd() + "\\advent_of_code\input2.txt") as f:
    data = f.read().strip().split(sep="\n")

horizontal_pos = 0
depth = 0
aim = 0

"""Part One"""
# for instruction in data:
#     instructionList = instruction.split(sep=" ")
#     move = instructionList[0]
#     value = int(instructionList[1])

#     if move == 'forward':
#         horizontal_pos += value
#     elif move == 'up':
#         depth -= value
#     elif move == 'down':
#         depth += value

# print(f"Horizontal position is {horizontal_pos}, and the depth is at {depth}.")
# print(horizontal_pos * depth)

"""Part two"""
for instruction in data:
    instructionList = instruction.split(sep=" ")
    move = instructionList[0]
    value = int(instructionList[1])

    if move == 'forward':
        horizontal_pos += value
        depth += aim * value

    elif move == 'up':
        aim -= value

    elif move == 'down':
        aim += value

print(horizontal_pos * depth)
