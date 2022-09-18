import makeLink as mk

def getData() -> list:
    with open(mk.makeInputLink(10)) as f:
        data = f.read().split('\n')
    return data

def partOne() -> int:
    return 0

def partTwo() -> int:
    return 0