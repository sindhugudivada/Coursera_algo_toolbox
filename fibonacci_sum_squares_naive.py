# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 0 :
       return n
    previous = 0
    current  = 1
    for i in range(n % 60):
        previous, current = current % 10, (previous + current) % 10
    return (previous * current) % 10

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_naive(n))
