import makeLink as mk

def getData() -> list:
    with open(mk.makeInputLink(10)) as f:
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


def partOne(data: list) -> int:
    scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
    total = 0
    for line in data:
        doOnce = checkCorrupted(line)
        if doOnce[0]:
            incorrect = doOnce[1]
            total += scores[incorrect]

    return total


def partTwo(data: list) -> int:
    scores = {'(': 1, '[': 2, '{': 3, '<': 4}
    totalScores = []
    
    for i in range(len(data)):
        doOnce = checkCorrupted(data[i])

        # only do if a line is not corrupted (cause we throw those out)
        if not doOnce[0]:
            current = doOnce[1]
            littleTotal = 0
            
            # traverse the current string backwards because i don't want to
            # reverse it and this is more efficient
            # then do the puzzle specifications and add that to a list
            for i in range(len(current) - 1, -1, -1):
                littleTotal *= 5
                littleTotal += scores[current[i]]
            
            totalScores.append(littleTotal)
    # puzzle calls for this, at least I don't have to write a sorting algo
    # myself AND I LOOKED IT UP THEY USE TIMSORT ITS NOT NAMED
    # after ME BUT HAS MY NAME IN IT THATS REALLY COOL
    totalScores.sort()

    return totalScores.pop(len(totalScores) // 2)