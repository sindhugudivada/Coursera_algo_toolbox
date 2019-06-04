# python3
import sys
from bisect import bisect_left

def takeClosest(myList, myNumber):
    pos = bisect_left(myList, myNumber)
    if pos == 0:
        return myList[0]
    if pos == len(myList):
        return myList[-1]
    before = myList[pos - 1]
    after = myList[pos]
    if after - myNumber < myNumber - before:
        return after
    else:
        return before

def compute_min_refills(distance, tank, stops):
    min_stops = 0
    next_index = 0
    new_value = 0
    length = len(stops)
    while next_index < length and new_value + tank < distance:
        min_stops += 1
        previous_value = new_value
        new_value = takeClosest(stops[next_index:], new_value+tank)
        next_index = stops.index(new_value)
        if previous_value == new_value:
           return -1
    return min_stops

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
