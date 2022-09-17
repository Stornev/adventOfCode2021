from makeLink import makeInputLink

# puzzle specs: https://pastebin.com/BkF4nGHj
# your own if you have an acct: https://adventofcode.com/2021/day/8
# puzzle specs
# 0 - abcefg
# 1 - cf
# 2 - acdeg
# 3 - acdfg
# 4 - bcdf
# 5 - abdfg
# 6 - abdefg
# 7 - acf
# 8 - abcdefg
# 9 - abcdfg

def getData():
    with open(makeInputLink(8)) as f:
        data = f.read().split('\n')

    return data

def partOne(data: list):
    """only 1,4,7,8 in output values (after |)"""
    numbers = {
        0: 'abcefg', 1: 'cf', 2: 'acdeg', 3: 'acdfg', 4: 'bcdf', 
        5: 'abdfg', 6: 'abdefg', 7: 'acf', 8: 'abcdefg', 9: 'abcdfg'
    }

    numbersLen = {i : len(numbers[i]) for i in range(0,10)}

    easyNums = {1: 2, 4: 4, 7: 3, 8: 7}
    countNums = {1: 0, 4: 0, 7: 0, 8: 0}
    
    for i in range(0, len(data)):
        data[i] = data[i].split('| ')[-1]

    for output in data:
        outputList = output.split(' ')
        for num in outputList:
            for easyNum in easyNums:
                if len(num) == easyNums[easyNum]:
                    countNums[easyNum] += 1

        
    return sum(countNums.values())

# necessary class for part two
class digitalNumber:
    # septem is latin prefix for seven, therefore should be used to represent
    # the first seven letters of the alphabet that is used in this puzzle
    SEPTEM = 'abcdefg'

    # these numbers never change, and always correspond this way
    # puzzle dictated this
    NUMBERS = {
        0: 'abcefg', 1: 'cf', 2: 'acdeg', 3: 'acdfg', 4: 'bcdf', 
        5: 'abdfg', 6: 'abdefg', 7: 'acf', 8: 'abcdefg', 9: 'abcdfg'
    }

    numAsDict = {}
    mapLetters = {}
    sensorData = ''
    outputData = ''
    outputNumbers = []
    

    def __init__(self, sensorData) -> None:
        self.sensorData = sensorData
        self.numAsDict = {i : self.SEPTEM[i] + ' ' for i in range(0,7)}
        self.outputData = sensorData.split(sep=" | ")[-1]
        
    
    def getSensorData(self) -> str:
        return self.sensorData

    def setMapLetters(self, mapLetters: dict) -> None:
        """sets the map of real : fake values"""
        
        self.mapLetters = mapLetters

    def printNumber(self) -> None:
        """prints the number with the correct mapping"""
        
        print(f"\n {self.numAsDict[0] * 4}")
        print(f"{self.numAsDict[1]}      {self.numAsDict[2]}")
        print(f"{self.numAsDict[1]}      {self.numAsDict[2]}")
        print(f" {self.numAsDict[3] * 4}")
        print(f"{self.numAsDict[4]}      {self.numAsDict[5]}")
        print(f"{self.numAsDict[4]}      {self.numAsDict[5]}")
        print(f" {self.numAsDict[6] * 4}\n")


    def sortString(self, outputNum: str) -> str:
        """Sorts a number string to alphabetical\n
           Ex. adb --> abd"""
        
        listOfOrd = []
        sortedNumAsStr = ''
        
        for letter in outputNum:
            listOfOrd.append(ord(letter))
        
        listOfOrd.sort()
        for num in listOfOrd:
            sortedNumAsStr += chr(num)

        return sortedNumAsStr

    def doesStrEqualNum(self, sortedOutputNum: str) -> bool:
        """determines if a sorted output number string is a valid number string"""
        
        flag = False
        for key in self.NUMBERS:
            if self.NUMBERS[key] == sortedOutputNum:
                flag = True
        
        return flag

    def doesOutputEqualNumbers(self) -> bool:
        """determines if all the output numbers are actual numbers\n
           True if so, False else"""

        current = self.outputData
        outputList = current.split(sep=" ")

        flagList = []
        for string in outputList:
            translatedString = self.translate(string)
            sortedString = self.sortString(translatedString)
            flagList.append(self.doesStrEqualNum(sortedString))

            # print(sortedString)
        return not False in flagList

    def mapNumAsDict(self) -> None:
        """this swaps the normal switch positions with their fake values\n
           Ex. if a --> c it is {0 : 'c'} in the dictionary, 0 is the value for a"""

        for key in self.numAsDict:
            keysAsList = list(self.mapLetters.keys())
            self.numAsDict[key] = self.mapLetters[keysAsList[key]] + ' '

    def translate(self, encoded: str) -> str:
        """translates an encoded fake value string to its correct letters\n
           though needs to have the right map to do so"""

        table = self.mapLetters
        translatedStr = ''
        tableValues = list(table.values())
        tableKeys = list(table.keys())
        
        for letter in encoded:
            index = tableValues.index(letter)
            translatedStr += tableKeys[index]
        
        return translatedStr

    def makeMap(self) -> dict:
        """makes the correct mapping from real characters to fake ones based
           exclusively on how the puzzle is organized for all lines"""
        map = {chr(i) : '' for i in range(97,104)}

        oneLetters = ''
        sevenLetters = ''
        fourLetters = ''
        fiveSuitable = ''
        inputAndOutputList = self.sensorData.split(" ")
        inputAndOutputList.remove('|')

        for string in inputAndOutputList:
            if len(string) == 2:
                oneLetters = string
            elif len(string) == 3:
                sevenLetters = string
            elif len(string) == 4:
                fourLetters = string
        
        # guaranteed letter here
        for letter in sevenLetters:
            if letter not in oneLetters:
                map['a'] = letter

        # find the or clause
        thisOrThat = fourLetters.replace(oneLetters[0], '') \
                                .replace(oneLetters[1], '')
        
        # finds the correct five letter number that 
        # can solve what is d and g and therefore b
        for string in inputAndOutputList:
            if (len(string) == 5 and 
                oneLetters[0] in string and 
                oneLetters[1] in string and 
                (thisOrThat[0] in string or thisOrThat[1] in string)):

                fiveSuitable = string
        
        # NUMBERS[2,3,5] are the three five letter numbers that we have to compare against
        # sike, it's always acf so it's always NUMBERS[3]

        dOrG = fiveSuitable.replace(sevenLetters[0], '') \
                           .replace(sevenLetters[1], '') \
                           .replace(sevenLetters[2], '')

        bOrD = fourLetters.replace(oneLetters[0], '') \
                          .replace(oneLetters[1], '')

        # find same letter in dOrG and in bOrD, that equals d
        # by figuring out what number is in both dOrG and bOrD
        # could use a for loop but its only 4 characters with 3 unique possibilities
        d = ''
        if dOrG[0] == bOrD[0]:
            d = bOrD[0]
        elif dOrG[0] == bOrD[1]:
            d = bOrD[1]
        elif dOrG[1] == bOrD[0]:
            d = bOrD[0]
        else:
            d = bOrD[1]
        map['d'] = d

        # find g out of all known numbers removed from fiveSuitable
        g = fiveSuitable.replace(map['a'], '') \
                        .replace(map['d'], '') \
                        .replace(oneLetters[0], '') \
                        .replace(oneLetters[1], '')
        map['g'] = g

        # find b by removing all known letters from fourLetters
        # only one left has to be b (puzzle characteristic)
        b = fourLetters.replace(map['a'], '') \
                       .replace(map['d'], '') \
                       .replace(map['g'], '') \
                       .replace(oneLetters[0], '') \
                       .replace(oneLetters[1], '')
        map['b'] = b
        
        # find fiveLettersWithMostInMap to figure out which one can solve f
        fiveMost = ''
        fivePossible = {'': 0}
        for item in inputAndOutputList:
            if len(item) == 5:
                occurences = 0
                
                for key in map:
                    if map[key] != '' and map[key] in item:
                        occurences += 1
                
                fivePossible.update({item: occurences})

        for key in fivePossible:
            if (fivePossible[key] != 5 and
                fivePossible[key] > fivePossible[fiveMost]):
                fiveMost = key

        # conincidentally fiveMost is always the number 5 (abdfg)
        # and we know every letter except what maps to f
        f = fiveMost.replace(map['a'], '') \
                    .replace(map['b'], '') \
                    .replace(map['d'], '') \
                    .replace(map['g'], '')
        map['f'] = f
        
        # now that we know f we can determine c with oneLetters
        # because cf -> one -> oneLetters <- is swapped chars and we know f
        # so which swapped char is c? the only remaining one after removing
        # the swapped char for f
        map['c'] = oneLetters.replace(map['f'], '')

        # what letter is not mapped? that letter is e
        # basic which letter is not there, that character has to be e
        # because it's the only one not left filled
        # this somehow works for all puzzle inputs
        septem = self.SEPTEM
        for key in map:
            septem = septem.replace(map[key], '')

        map['e'] = septem

        return map

    def makeOutputNum(self) -> int:
        """Precondition: run map = makeMap, setMapLetters(map) on this object\n
        This converts the letter representations of the output into their
        corresponding output number given what each character is supposed to be"""
        
        # convert the numbers in the output to the real values
        outputList = self.outputData.split(" ")
        translatedList = []
        for num in outputList:
            translatedList.append(self.translate(num))

        # sort these values in alphabetical order to correctly 
        # identify the numbers
        sortedList = []
        for num in translatedList:
            sortedList.append(self.sortString(num))

        # convert the sorted letter number list into a plain list of ints
        # such that the letter numbers equal their int counterpart
        numList = []
        for num in sortedList:
            for key in self.NUMBERS:
                if self.NUMBERS[key] == num:
                    numList.append(key)

        # convert the list of ints into a full larger integer
        # because of the puzzle's specifications
        strNum = ''
        for num in numList:
            strNum += str(num)
        
        return int(strNum)


def partTwo(data: list):
    digitalNumberList = []
    for line in data:
        digitalNumberList.append(digitalNumber(line))

    total = 0
    for i in range(0, len(digitalNumberList)):
        map = digitalNumber.makeMap(digitalNumberList[i])
        digitalNumber.setMapLetters(digitalNumberList[i], map)
        total += digitalNumber.makeOutputNum(digitalNumberList[i])
        # to print the four digit seven segment display of every display
        # digitalNumber.mapNumAsDict(digitalNumberList[i])
        # digitalNumber.printNumber(digitalNumber[i])
    
    return total