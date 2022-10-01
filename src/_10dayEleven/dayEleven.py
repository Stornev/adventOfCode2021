import makeLink as mk

def getData():
    with open(file=mk.makeTestInputLink(11)) as f:
        data = f.read().split('\n')
    
    return data

class Octopus:
    def __init__(self, value: int) -> None:
        self.value = value
        self.hasFlashed = False
    
    @property
    def value(self) -> int:
        return self._value
    
    @value.setter
    def value(self, other: int):
        self._value = other

    @property
    def hasFlashed(self) -> bool:
        return self._hasFlashed

    @hasFlashed.setter
    def hasFlashed(self, other: bool):
        self._hasFlashed = other

class OctopusBoard:
    def __init__(self, data: list, step: int) -> None:
        self.board = [[Octopus(int(data[j][i])) for i in range(10)] for j in range(10)]
        self.step = step

    def increaseAll(self):
        self.board = [[Octopus(self.board[j][i].value + 1) for i in range(10)] for j in range(10)]

    def printBoard(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print(str(self.board[i][j].value), end='  ')
            print('\n')

    def clearFlash(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.board[i][j].hasFlashed = False

    def checkIfCanFlash(self) -> list:
        retList = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j].value > 9:
                    retList.append((i, j))
        return retList

    def findAdjacent(self, pos) -> list:
        pass

    def onFlash(self, pos) -> int:
        # all adjacent also increase by one
        # if this makes the octopus also > 9, it also flashes
        # can only flash once per step
        adjacents = self.findAdjacent(pos)
        master = [adjacent for adjacent in adjacents]
        master.append((pos[0], pos[1]))
    

def partOne(data: list):
    board = OctopusBoard(data, 0)
    total = 0
    for i in range(1,3):
        board.step = i
        board.increaseAll()
        flashers = board.checkIfCanFlash()
        for flash in flashers:
            total += board.onFlash(flash)
    return None

def partTwo(data: list):
    return 0 

if __name__ == '__main__':
    import testOneDay