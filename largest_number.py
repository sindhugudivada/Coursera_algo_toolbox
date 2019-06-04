#Uses python3

import sys
from functools import cmp_to_key

def largest_number(a):
    a = [str(digit) for digit in a]
    a.sort(key = cmp_to_key(compare_string), reverse = True)
    res = ''.join(a)
    return res

def compare_string(x,y):
    if x + y > y + x:
       return 1
    elif x == y:
       return 0
    else:
       return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
