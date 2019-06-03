#!/usr/bin/python
import sys

def get_change(m):
    coinsCount = 0
    while m != 0:
        if m % 10 == 0:
           m = m - 10
           coinsCount += 1
        elif m % 5 == 0:
           m = m - 5
           coinsCount += 1
        else:
           m = m - 1
           coinsCount += 1
    return coinsCount

if __name__ == '__main__':
    #m = int(sys.stdin.read())
    print(get_change(40))
