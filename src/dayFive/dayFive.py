import os


"""Part One"""
class line:
    firstCoords = []
    secondCoords = []

    def __init__(self, lineStr: str) -> None:
        self.firstCoords = lineStr.split(sep=" -> ")[0].split(sep=",")
        self.secondCoords = lineStr.split(sep=" -> ")[1].split(sep=",")
    
    # x1, y1 -> x2, y2
    def horizontalOrVertical(self):
        if self.firstCoords[0] == self.secondCoords[0]:
            return 'vertical'
        elif self.firstCoords[1] == self.secondCoords[1]:
            return 'horizontal'
        else:
            return 'diagonal'

    # Part two
    def getLine(self):
        return self.firstCoords, self.secondCoords

class board:
    baseBoard = [['.' for i in range(0, 1000)] for x in range(0, 1000)]

    
    def __init__(self) -> None:
        pass

    def getBoard(self):
        return self.baseBoard

    # x = 0-1000 y = 0-1000
    def drawDiagram(self):
        with open("advent_of_code\output5.txt", "w") as f:
            for row in self.baseBoard:
                for column in row:
                    f.write(column)
                f.write("\n")


    # x1, y1 -> x2, y2
    def putLineOnBoard(self, currentLine: line):
        horOrVer = line.horizontalOrVertical(currentLine)

        if horOrVer == 'horizontal':
            x1 = int(currentLine.firstCoords[0])
            x2 = int(currentLine.secondCoords[0])
            big = max(x1, x2)
            notBig = min(x1, x2)
            horizontalCoord = int(currentLine.firstCoords[1])
            
            # for the range of the length of the line (inclusive)
            for i in range(notBig, big + 1):
                # line on file will not be equal to horizontalCoord
                # but will be equivalent whenever called
                if self.baseBoard[horizontalCoord][i] == '.':
                    self.baseBoard[horizontalCoord][i] = '1'
                else:
                    upOne = int(self.baseBoard[horizontalCoord][i]) + 1
                    self.baseBoard[horizontalCoord][i] = str(upOne)


        elif horOrVer == 'vertical':
            y1 = int(currentLine.firstCoords[1])
            y2 = int(currentLine.secondCoords[1])
            big = max(y1, y2)
            notBig = min(y1, y2)
            verticalCoord = int(currentLine.firstCoords[0])
            
            # for the range of the length of the line (inclusive)
            for i in range(notBig, big + 1):
                # line on file will not be equal to verticalCoord
                # but will be equivalent whenever called
                if self.baseBoard[i][verticalCoord] == '.':
                    self.baseBoard[i][verticalCoord] = '1'
                else:
                    upOne = int(self.baseBoard[i][verticalCoord]) + 1
                    self.baseBoard[i][verticalCoord] = str(upOne)

        # Part two     
        elif horOrVer == 'diagonal':
            x1 = int(currentLine.firstCoords[0])
            x2 = int(currentLine.secondCoords[0])
            y1 = int(currentLine.firstCoords[1])
            y2 = int(currentLine.secondCoords[1])

            if x1 > x2:
                xCoordsList = [i for i in range(x1, x2 -1, -1)]
            else:
                xCoordsList = [i for i in range(x1, x2 + 1)]

            if y1 > y2:
                yCoordsList = [i for i in range(y1, y2 -1, -1)]
            else:
                yCoordsList = [i for i in range(y1, y2 + 1)]

            for index in range(len(xCoordsList)):
                xIndex = xCoordsList[index]
                yIndex = yCoordsList[index]

                if self.baseBoard[yIndex][xIndex] == '.':
                    self.baseBoard[yIndex][xIndex] = '1'
                else:
                    upOne = int(self.baseBoard[yIndex][xIndex]) + 1
                    self.baseBoard[yIndex][xIndex] = str(upOne)


with open(file= os.getcwd() + "\\advent_of_code\\input5.txt") as f:
    data = f.read().strip().split(sep="\n")

myBoard = board()

for row in data:
    currentLine = line(row)
    board.putLineOnBoard(myBoard, currentLine)

boardAsList = board.getBoard(myBoard)

moreThanTwo = 0
for row in boardAsList:
    for item in row:
        if item != '.':
            value = int(item)
            if value >= 2:
                moreThanTwo += 1
            

print(moreThanTwo)
board.drawDiagram(myBoard)
