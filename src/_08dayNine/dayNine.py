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

    # add first line padding and last line padding
    data.insert(0, ' ' * len(data[0]))
    data.insert(len(data), ' ' * len(data[0]))

    return data

def writeDataToFile() -> None:
    data = getData()
    with open(file=makeLink.makeOutputLink(9), mode='w') as f:
        for i in range(0, len(data)):
            if i != len(data) - 1:
                f.write(data[i] + '\n')
            else:
                f.write(data[i])
            

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
        above = self.board[row - 1][col]
        below = self.board[row + 1][col]
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
    
    # make all inpassable of basin an X
    # defunct, was for visualization of all the basins
    def makeAllNineChi(self):
        for i in range(len(self.board)):
            for x in range(len(self.board[i])):
                if self.board[i][x] == '9':
                    self.board[i] = self.board[i].replace('9', chr(88))

    # return a list of tuples that correspond to all the points in a basin
    # the values in the tuples will be a coordinate pair of (row, column)
    # that correspond to their position in self.board
    def exploreBasin(self, lowpoint: tuple) -> list:
        row = lowpoint[0]
        col = lowpoint[1]
        # initial exploration
        posList = self.exploreBranch((row, col))

        # main exploration
        bigCache = []
        
        for tuple in posList:
            # add inital lowPoint tuples
            bigCache.append(tuple)
        
        previousLength = -1
        while self.isDone(bigCache, previousLength):
            for tuple in bigCache:
                previousLength = len(bigCache)
                littleCache = self.exploreBranch((tuple[1][0], tuple[1][1]))
                
                for element in littleCache:
                    if element not in bigCache:
                        bigCache.append(element)
            
        return bigCache

    def isDone(self, cache: list, previous: int):
        currentLength = len(cache)
        if previous == -1:
            # continues to run if first occurence
            return True

        elif previous == currentLength:
            # should mean that there is no more exploration to do
            return False

        # in all other cases continue to run
        return True

    # explore a branch of the basin (one way the basin can go)
    def exploreBranch(self, branch: tuple):
        row = branch[0]
        col = branch[1]
        above = self.board[row - 1][col]
        below = self.board[row + 1][col]
        left = self.board[row][col - 1]
        right = self.board[row][col + 1]

        posList = [
            (above, (row - 1, col)), (below, (row + 1, col)),
            (left, (row, col - 1)), (right, (row, col + 1))
        ]

        posListValues = [above, below, left, right]
        
        index = 0
        while ' ' in posListValues or '9' in posListValues:
            value = posList[index][0]

            if value == ' ' or value == '9':
                posList.remove(posList[index])
                posListValues.remove(posListValues[index])
                index -= 1

            index += 1
        
        return posList
        
def partOne(data: list) -> int:
    myBoard = smokeBoard(data)
    sumOfRisk = 0

    for i in range(1, len(data) - 1):
        for x in range(1, len(data[i]) - 1):
            if smokeBoard.checkIfLowpoint(myBoard, i, x):
                risk = int(data[i][x]) + 1
                sumOfRisk += risk

    return sumOfRisk

# don't ask me how the hell this works
# and this has to be the most inefficient way to do this but it works?!
def partTwo(data: list) -> int:
    myOtherBoard = smokeBoard(data)

    lowPoints = []
    for i in range(1, len(data) - 1):
        for x in range(1, len(data[i]) - 1):
            if smokeBoard.checkIfLowpoint(myOtherBoard, i, x):
                lowPoints.append((i,x))

    listOfBasins = []
    for lowPoint in lowPoints:
        listOfBasins.append(smokeBoard.exploreBasin(myOtherBoard, lowPoint))

    listOfLengths = [len(basin) for basin in listOfBasins]
    listOfLengths.sort()
    threeLargest = listOfLengths[-1] * listOfLengths[-2] * listOfLengths[-3]

    return threeLargest