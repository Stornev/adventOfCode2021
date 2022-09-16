from makeLink import makeInputLink

def getData():
    with open(file=makeInputLink(2)) as f:
        data = f.read().strip().split(sep="\n")

    return data


def partOne(data: list):
    horizontal_pos = 0
    depth = 0

    for instruction in data:
        instructionList = instruction.split(sep=" ")
        move = instructionList[0]
        value = int(instructionList[1])

        if move == 'forward':
            horizontal_pos += value
        elif move == 'up':
            depth -= value
        elif move == 'down':
            depth += value
    
    return (horizontal_pos, depth)


def partTwo(data: list):
    horizontal_pos = 0
    depth = 0
    aim = 0

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

    return [horizontal_pos, depth, aim]
