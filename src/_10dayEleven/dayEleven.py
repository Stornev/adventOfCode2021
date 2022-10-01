import makeLink as mk

def getData():
    with open(file=mk.makeTestInputLink(11)) as f:
        data = f.read().split('\n')
    
    return data

class OctopusBoard:
    def __init__(self, data: list) -> None:
        self.board = [[int(data[j][i]) for i in range(10)] for j in range(10)]

    def increaseAll(self):
        self.board = [[self.board[j][i] + 1 for i in range(10)] for j in range(10)]

    def printBoard(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print(str(self.board[i][j]), end='  ')
            print('\n')

def partOne(data: list):
    board = OctopusBoard(data)
    board.increaseAll()
    board.increaseAll()
    board.printBoard()
    return 0

def partTwo(data: list):
    return 0 

if __name__ == '__main__':
    import testOneDay