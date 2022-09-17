import makeLink
import termcolor

def getData() -> list:
    with open(makeLink.makeInputLink(9)) as f:
        data = f.read().split('\n')

    # add data padding
    for i in range(len(data)):
        correct = ' '
        for num in data[i]:
            correct += num
        correct += ' '
        data[i] = correct

    data.insert(0, ' ' * 102)
    data.insert(101, ' ' * 102)

    return data

def writeDataToFile() -> None:
    data = getData()
    with open(file=makeLink.makeOutputLink(9), mode='w') as f:
        for line in data:
            if data.index(line) != 100:
                f.write(line + '\n')
            else:
                f.write(line)
            

class smokeBoard:
    rawData = []
    board = [[] for i in range(0,102)]

    def __init__(self, data: list) -> None:
        self.rawData = data

        for i in range(0, len(data)):
            self.board[i] = data[i]
        
    def printBoard(self) -> None:
        for row in self.board:
            for col in row:
                if col == chr(88):
                    print(termcolor.colored(col, 'blue', attrs=['bold']), end='')
                else:
                    print(col, end='')
            print()

    def checkIfLowpoint(self, row: int, col: int) -> bool:
        # given that current is not ' '
        current = self.board[row][col]
        above = self.board[row + 1][col]
        below = self.board[row - 1][col]
        left = self.board[row][col - 1]
        right = self.board[row][col + 1]

        posList = [above, below, left, right]

        # make sure all are actual values and not ' '
        for unknown in posList:
            if unknown == ' ':
                posList.remove(unknown)

        # make sure they're not all the same value
        setOfPos = set(posList)

        # if the list only contains one value
        # then see if the current is lowest or not
        # by seeing if one item in list is less than the current
        if len(setOfPos) == 1 and current >= posList[0]:
            return False

        # find least
        posList.append(current)
        least = min(posList)

        # if current is low point ret T else F
        if least == current:
            return True
        return False
    
    def makeAllNineChi(self):
        for i in range(len(self.board)):
            for x in range(len(self.board[i])):
                if self.board[i][x] == '9':
                    self.board[i] = self.board[i].replace('9', chr(88))

        
def partOne(data: list) -> int:
    myBoard = smokeBoard(data)
    sumOfRisk = 0

    for i in range(1, len(data) - 1):
        for x in range(1, len(data[i]) - 1):
            if smokeBoard.checkIfLowpoint(myBoard, i, x):
                risk = int(data[i][x]) + 1
                sumOfRisk += risk

    return sumOfRisk
            
def partTwo(data: list) -> int:
    myOtherBoard = smokeBoard(data)
    smokeBoard.makeAllNineChi(myOtherBoard)
    smokeBoard.printBoard(myOtherBoard)
    return 0