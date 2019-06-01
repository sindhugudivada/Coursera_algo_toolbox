# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 0 :
       return n
    insights = {0:0,1:1,2:4,3:9,4:6,5:5,6:6,7:9,8:4,9:1}
    last_sum_cache = [[(i+j) % 10 for i in range(10)] for j in range(10)]
    previous = 0
    current  = 1
    sum      = 0
    for i in range(n):
        previous, current = current % 10, (previous + current)%10
        sum = sum % 10 + insights[previous]
        return sum % 10

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_naive(n))
