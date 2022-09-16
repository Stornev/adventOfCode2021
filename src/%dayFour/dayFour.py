from os import getcwd

with open(file= getcwd() + "\\src\\\%dayFour\\input4.txt") as f:
    data = f.read().strip().split(sep="\n\n")

# board is cool
class bingoBoard:
    board = [[]]

    def __init__(self, boardNumbers: str):
        self.board = [[0 for i in range(0,5)] for y in range(0,5)]

        listOfNumbers = boardNumbers.split(sep='\n')
        
        for i in range(0, 5):
            row = listOfNumbers[i].strip().split(sep=' ')
            
            for x in range(0, 5):
                while '' in row:
                    row.remove('')
                
                currentNum = int(row[x])
                self.board[i][x] = currentNum

    def printBoard(self):
        for i in range(0,5):
            for x in range(0,5):
                print("{0:<3}".format(self.board[i][x]), end=" ")
            print()

    def getBoard(self):
        return self.board

    def fillSpot(self, row: int, col: int):
        self.board[row][col] = -1

    def printSpot(self, row: int, col: int):
        print(self.board[row][col])

    def findNumInBoard(self, num: str):
        num = int(num)
        for row in self.board:
            if num in row:
                return (self.board.index(row), row.index(num))
            
        return False

    def checkIfWon(self):
        for i in range(0,5):
            horizontalFilled = 0
            verticalFilled = 0
            row = self.board[i]

            for x in range(0,5):
                column = self.board[x][i]
                numInRow = row[x]

                if column == -1:
                    verticalFilled += 1

                if numInRow == -1:
                    horizontalFilled += 1

            if horizontalFilled == 5 or verticalFilled == 5:
                return True
        return False


"""Part One"""
numbersChosen = data.pop(0).split(sep=',')

boardList = []
for i in range(0, len(data)):
    boardList.append(bingoBoard(data[i]))

# for num in numbersChosen:
#     for board in boardList:
#         indexTuple = bingoBoard.findNumInBoard(board, num)
#         if type(indexTuple) == tuple:
#             bingoBoard.fillSpot(board, indexTuple[0], indexTuple[1])
    
#     for board in boardList:
#         if bingoBoard.checkIfWon(board):
#             sum = 0
#             wonBoard = bingoBoard.getBoard(board)

#             for i in range(0,5):
#                 for x in range(0,5):
#                     if wonBoard[i][x] != -1:
#                         sum += wonBoard[i][x]
#             print(sum * int(num))
#             print()
#             exit()

"""Part Two"""
numOfBoards = len(data)

listOfBoardsWon = []
for num in numbersChosen:
    for board in boardList:
        indexTuple = bingoBoard.findNumInBoard(board, num)
        if type(indexTuple) == tuple:
            bingoBoard.fillSpot(board, indexTuple[0], indexTuple[1])
    
    
    for board in boardList:
        if board not in listOfBoardsWon and bingoBoard.checkIfWon(board):
            listOfBoardsWon.append(board)

            if len(listOfBoardsWon) == 100:    
                sum = 0
                wonBoard = bingoBoard.getBoard(board)

                for i in range(0,5):
                    for x in range(0,5):
                        if wonBoard[i][x] != -1:
                            sum += wonBoard[i][x]
                print(sum * int(num))
