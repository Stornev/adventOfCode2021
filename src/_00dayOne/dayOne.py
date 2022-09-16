from makeLink import makeInputLink

def getData():
    with open(file=makeInputLink(1)) as f:
        data = f.read().strip().split(sep="\n")

    return data


def partOne(data: list):
    counter = 0
    for i in range(0, len(data) - 1):
        first = int(data[i])
        second = int(data[i+1])
        if first < second:
            counter += 1

    return counter

def partTwo(data: list):
    sum_of_measurements = []

    for i in range(0, len(data) - 2):
        measurement_one = int(data[i])
        measurement_two = int(data[i+1])
        measurement_three = int(data[i+2])

        sum_of_measurements.append(measurement_one
                                + measurement_two
                                + measurement_three)

    counter = 0

    for i in range(0, len(sum_of_measurements) - 1):
        one = sum_of_measurements[i]
        two = sum_of_measurements[i+1]

        if one < two:
            counter += 1

    return counter

if __name__ == '__main__':
    partOne(data)
    partTwo(data)