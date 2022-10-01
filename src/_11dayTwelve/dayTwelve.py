def getData():
    import makeLink as mk
    with open(file=mk.makeTestInputLink(12)) as f:
        data = f.read().split('\n')
    
    return data

def partOne(data: list):
    return 0

def partTwo(data: list):
    return 0