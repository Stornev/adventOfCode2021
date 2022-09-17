import makeLink

def getData():
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

def writeDataToFile():
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

    def __init__(self, data: list):
        self.rawData = data

        for i in range(0, len(data)):
            self.board[i] = data[i]
        
    def printBoard(self):
        for row in self.board:
            for col in row:
                print(col, end='')
            print()

    def checkIfLowpoint(self, row: int, col: int) -> bool:
        above = self.board[row + 1][col]
        below = self.board[row - 1][col]
        left = self.board[row][col - 1]
        right = self.board[row][col + 1]

        
def partOne(data: list):
    myBoard = smokeBoard(data)
    for i in range(1, len(data) - 1):
        for x in range(1, len(data[i]) - 1):
            smokeBoard.checkIfLowpoint(myBoard, i, x)
