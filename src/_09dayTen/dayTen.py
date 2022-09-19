import makeLink as mk

def getData() -> list:
    with open(mk.makeInputLink(10)) as f:
        data = f.read().split('\n')
    return data

closing = {'(': ')', '[': ']', '{': '}', '<': '>'}
partners = {')': '(', ']': '[', '}': '{', '>': '<'}

def isClosing(char: str):
    """In order for this to run correctly I have to make sure that I know what
       a valid closing character is\n Returns T/F"""
    flag = False
    for key in partners:
        if key == char:
            flag = True
    return flag

def checkPartner(line: str, char: str) -> tuple:
    """Does the ending character have a romantic partner?\n
       Returns T/F if the character has a partner, and the supposed partner"""
    partner = ''
    # find if there is a closing character of the character
    index = line.find(closing[char])
    if index == -1:
        # if there is no closing character this is just incomplete
        return (False, 'incomplete')


    if char == partners[partner]:
        return (True, partner)
    else:
        return (False, partner)

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
    
    
    return (False, '')

scores = {')': 3, ']': 57, '}': 1197, '>': 25137}

def partOne(data: list) -> int:
    total = 0
    for line in data:
        doOnce = checkCorrupted(line)
        if doOnce[0]:
            incorrect = doOnce[1]
            total += scores[incorrect]


    return total

def partTwo(data: list) -> int:
    return 0