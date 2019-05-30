# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if (n <= 1):
        return n
    firstTerm = 0
    secondTerm = 1
    count = 1
    while count < n:
        total = firstTerm % 10 + secondTerm % 10
        firstTerm = secondTerm % 10
        secondTerm = total % 10
        count += 1
    return total % 10
