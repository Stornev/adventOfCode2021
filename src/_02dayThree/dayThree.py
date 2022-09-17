from makeLink import makeInputLink

def getData():
    with open(file=makeInputLink(3)) as f:
        data = f.read().strip().split(sep="\n")

    return data

def partOne(data: list) -> int:
    gamma_rate = ''
    epsilon_rate = ''

    columnsOne = {
        1 : 0, 2 : 0, 3 : 0, 4 : 0, 
        5 : 0, 6 : 0, 7: 0, 8 : 0, 
        9 : 0, 10 : 0, 11 : 0, 12 : 0
    }

    columnsZero = {
        1 : 0, 2 : 0, 3 : 0, 4 : 0, 
        5 : 0, 6 : 0, 7: 0, 8 : 0, 
        9 : 0, 10 : 0, 11 : 0, 12 : 0
    }

    for i in range(0, len(data)):
        current = data[i]

        for x in range(0, len(data[i])):
            num = int(current[x])

            if num == 1:
                columnsOne[x+1] += 1
            elif num == 0:
                columnsZero[x+1] += 1

    for y in range(1, 13):

        if columnsOne[y] > columnsZero[y]:
            gamma_rate += '1'
            epsilon_rate += '0'
        else:
            gamma_rate += '0'
            epsilon_rate += '1'

    return int(gamma_rate, 2) * int(epsilon_rate, 2)

def mostCommonBit(binaryList: list, column: int):
    ones = 0
    zeroes = 0
    for i in range(0, len(binaryList)):
        if binaryList[i][column] == '1':
            ones += 1
        else:
            zeroes += 1

    return '1' if ones >= zeroes else '0'

def partTwo(data: list):
    co2 = data.copy()

    for i in range(0, 12):
        delete = []
        deleteCO2 = []
        most_common_bit = mostCommonBit(data, i)
        least_common_bit = '1' if mostCommonBit(co2, i) == '0' else '0'

        for line in data:
            if line[i] != most_common_bit and line not in delete:
                delete.append(line)

        for item in delete:
            data.remove(item)

        for bits in co2:
            if bits[i] != least_common_bit and bits not in deleteCO2:
                deleteCO2.append(bits)

        if len(co2) != 1:
            for bit in deleteCO2:
                co2.remove(bit)
            
    return int(data[0], 2) * int(co2[0], 2)
