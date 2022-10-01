from os import getcwd

def makeInputLink(day: int):
    numbersToWords = {
        1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 
        7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Eleven', 
        12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 
        16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen',
        20: 'Twenty', 21: 'TwentyOne', 22: 'TwentyTwo', 23: 'TwentyThree',
        24: 'TwentyFour', 25: 'TwentyFive'
    }
    
    base = getcwd() + '\\src\\_'
    if day <= 10:
        base += str(0)
    baseDay = base + str(day - 1) + 'day' + numbersToWords[day]
    
    return baseDay + '\\input' + str(day) + '.txt'

def makeOutputLink(day: int):
    base = makeInputLink(day)
    link = base.replace('input', 'output')
    return link

def makeTestInputLink(*args):
    return getcwd() + '\\src\\testinput.txt'