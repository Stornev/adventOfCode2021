import _00dayOne.dayOne as d1
import _01dayTwo.dayTwo as d2
import _02dayThree.dayThree as d3
import _03dayFour.dayFour as d4
import _04dayFive.dayFive as d5
import _05daySix.daySix as d6
import _06daySeven.daySeven as d7
import _07dayEight.dayEight as d8
import _08dayNine.dayNine as d9
import _09dayTen.dayTen as d10

data1 = d1.getData()
data2 = d2.getData()
data3 = d3.getData()
data4 = d4.getData()
data5 = d5.getData()
data6 = d6.getData()
data7 = d7.getData()
data8p1 = d8.getData()
data8p2 = d8.getData()
data9 = d9.getData()
data10 = d10.getData()


print(f'Day 1 Part One: {str(d1.partOne(data1))}')
print(f'Day 1 Part Two: {str(d1.partTwo(data1))}\n')

d2Tuple = d2.partOne(data2)
d2p1Answer = str(d2Tuple[0] * d2Tuple[1])
print(f'Day 2 Part One: {d2p1Answer}')

d2List = d2.partTwo(data2)
d2p2Answer = str(d2List[0] * d2List[1])
print(f'Day 2 Part Two: {d2p2Answer}\n')

print(f'Day 3 Part One: {d3.partOne(data3)}')
print(f'Day 3 Part Two: {d3.partTwo(data3)}\n')

print(f'Day 4 Part One: {d4.partOne(data4)}')
print(f'Day 4 Part One: {d4.partTwo(data4)}\n')

print(f'Day 5 Part One: {d5.partOne(data5)}')
print(f'Day 5 Part Two: {d5.partTwo(data5)}\n')

print(f'Day 6 Part One: {d6.partOne(data6)}')
# this solution seems pretty slow
# but is faster than the first one I tried
# the first one wouldn't finish for likely hours
# calculating trillions of numbers is not easy
print(f'Day 6 Part Two: {d6.partTwo(data6)}\n')

# and these are extra slow, but do work
print(f'Day 7 Part One: {d7.partOne(data7)}')
print(f'Day 7 Part Two: {d7.partTwo(data7)}\n')

# this is v fast compared to the puzzles above lol
# but also like 300 more lines
print(f'Day 8 Part One: {d8.partOne(data8p1)}')
print(f'Day 8 Part Two: {d8.partTwo(data8p2)}\n')

# not as slow as the others but is it efficient?
print(f'Day 9 Part One: {d9.partOne(data9)}')
print(f'Day 9 Part Two: {d9.partTwo(data9)}\n')

#TODO add more days if I've completed them below