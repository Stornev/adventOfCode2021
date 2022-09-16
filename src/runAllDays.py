from makeLink import makeInputLink
import _00dayOne.dayOne as d1
import _01dayTwo.dayTwo as d2
import _02dayThree.dayThree as d3
import _01dayTwo.dayTwo as d2
import _01dayTwo.dayTwo as d2
import _01dayTwo.dayTwo as d2

data1 = d1.getData()
data2 = d2.getData()


print(f'Day 1 Part One: {str(d1.partOne(data1))}')
print(f'Day 1 Part Two: {str(d1.partTwo(data1))}\n')

d2Tuple = d2.partOne(data2)
d2p1Answer = str(d2Tuple[0] * d2Tuple[1])
print(f'Day 2 Part One: {d2p1Answer}')

d2List = d2.partTwo(data2)
d2p2Answer = str(d2List[0] * d2List[1])
print(f'Day 2 Part Two: {d2p2Answer}\n')




