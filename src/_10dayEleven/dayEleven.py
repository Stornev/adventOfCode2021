import makeLink as mk

def getData():
    with open(file=mk.makeInputLink(11)) as f:
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
    def value(self, other: int) -> None:
        self._value = other

    @property
    def hasFlashed(self) -> bool:
        return self._hasFlashed

    @hasFlashed.setter
    def hasFlashed(self, other: bool) -> None:
        self._hasFlashed = other

class OctopusBoard:
    def __init__(self, data: list, step: int) -> None:
        self.board = [[Octopus(int(data[j][i])) for i in range(len(data[j]))] for j in range(len(data))]
        self.step = step
        self.board.insert(0, [Octopus(-1) for i in range(len(data[1]))])
        self.board.append([Octopus(-1) for i in range(len(data[1]))])

        for row in self.board:
            row.insert(0, Octopus(-1))
            row.append(Octopus(-1))

    def increaseAll(self) -> None:
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j].value != -1:
                    self.board[i][j].value += 1

    def printBoard(self) -> None:
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j].value > 9:
                    print(str(self.board[i][j].value), end='  ')
                elif self.board[i][j].value == -1:
                     print('~', end='   ')
                else:
                    print(str(self.board[i][j].value), end='   ')
            print('\n')

    def printValues(self) -> None:
        for i in range(1, len(self.board) - 1):
            for j in range(1, len(self.board[i]) - 1):
                print(str(self.board[i][j].value), end='')
            print()

    def clearFlash(self) -> None:
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.board[i][j].hasFlashed = False

    def ifFlashedZero(self) -> int:
        total = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j].hasFlashed:
                    self.board[i][j].value = 0
                    total += 1
        return total

    def checkIfCanFlash(self) -> list:
        retList = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j].value > 9:
                    retList.append((i, j))
        return retList

    def findAdjacent(self, pos) -> list:
        # pos -> (row, col)
        # up            row+1 col    down          row-1 col
        # left          row   col-1  right         row   col+1
        # diagupleft    row+1 col-1  diagupright   row+1 col+1
        # diagdownleft  row-1 col-1  diagdownright row-1 col+1
        row = pos[0]
        col = pos[1]
        up = (row + 1, col)
        down = (row - 1, col)
        left = (row, col - 1)
        right = (row, col + 1)
        diagupleft = (row + 1, col - 1)
        diagupright = (row + 1, col + 1)
        diagdownleft = (row - 1, col - 1)
        diagdownright = (row - 1, col + 1)
        
        adjacents = [
            up, down, left, right, diagupleft, 
            diagupright, diagdownleft, diagdownright
        ]
        
        adjacents = [
            item for item in adjacents 
            if self.board[item[0]][item[1]].value != -1
        ]
        
        return adjacents

    def onFlash(self, pos) -> None:
        # all adjacent also increase by one
        # if this makes the octopus also > 9, it also flashes
        # can only flash once per step
        adjacents = self.findAdjacent(pos)
        octopus = self.board[pos[0]][pos[1]]
        octopus.hasFlashed = True

        for adjacent in adjacents:
            theirOctopus = self.board[adjacent[0]][adjacent[1]]
            theirOctopus.value += 1
            if theirOctopus.value > 9 and not theirOctopus.hasFlashed:
                self.onFlash((adjacent[0], adjacent[1]))

        # for item in adjacents:
        #     print(self.board[item[0]][item[1]].value, end=" ")
        # print(f'\n {pos}')
        # master.append((pos[0], pos[1]))
    

def partOne(data: list) -> int:
    board = OctopusBoard(data, 0)
    total = 0
    for i in range(1,101):
        # board.step = i
        board.increaseAll()
        flashers = board.checkIfCanFlash()
        for flash in flashers:
            if not board.board[flash[0]][flash[1]].hasFlashed:
                board.onFlash(flash)
        total += board.ifFlashedZero()
        board.clearFlash()
    # board.printValues()
    return total

def partTwo(data: list) -> int:
    board = OctopusBoard(data, 0)
    flashes = 0
    for i in range(1,252):
        # board.step = i
        board.increaseAll()
        flashers = board.checkIfCanFlash()
        for flash in flashers:
            if not board.board[flash[0]][flash[1]].hasFlashed:
                board.onFlash(flash)
        flashes = board.ifFlashedZero()
        if flashes == 100:
            # board.printValues()
            return i
        board.clearFlash()
    return None

if __name__ == '__main__':
    print("don't run me directly dummy!")