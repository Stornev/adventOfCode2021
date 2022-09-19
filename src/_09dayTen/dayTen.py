import makeLink as mk

def getData() -> list:
    with open(mk.makeTestInputLink()) as f:
        data = f.read().split('\n')
    return data

partners = {')': '(', ']': '[', '}': '{', '>': '<'}

def isClosing(char: str):
    """In order for this to run correctly I have to make sure that I know what
       a valid closing character is\n Returns T/F"""
    flag = False
    for key in partners:
        if key == char:
            flag = True
    return flag

def checkCorrupted(line: str) -> tuple:
    """Check if the line is corrupted, which means an ending character is the
       wrong one, not just not there\nReturns T/F and the incorrect character"""
    lengthPrevious = -1
    lengthBefore = -2
    while lengthPrevious != lengthBefore:
        lengthBefore = len(line)
        line = line.replace('()', '').replace('[]', '').replace('{}', '').replace('<>', '')
        lengthPrevious = len(line)
    
    for i in range(len(line) - 1):
        current = line[i]
        next = line[i+1]

        if isClosing(next) and partners[next] != current:
            return (True, next)
    
    
    return (False, line)

scores = {')': 3, ']': 57, '}': 1197, '>': 25137}

def partOne(data: list) -> int:
    total = 0
    for line in data:
        doOnce = checkCorrupted(line)
        if doOnce[0]:
            incorrect = doOnce[1]
            total += scores[incorrect]


    return total

scores = {'(': 1, '[': 2, '{': 3, '<': 4}

def partTwo(data: list) -> int:
    goodData = []
    for i in range(len(data)):
        doOnce = checkCorrupted(data[i])
        # print(data[i], doOnce)
        if doOnce[0]:
            pass
        else:
            current = doOnce[1]
            goodData.append(current)
            for i in range(len(goodData)):
                pass
        

    return goodData