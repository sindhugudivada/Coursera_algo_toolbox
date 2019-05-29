def calc_fib(n):
    if (n <= 1):
        return n
    firstTerm = 0
    secondTerm = 1     
    count = 0
    while count < n:
      total = firstTerm + secondTerm
      firstTerm = secondTerm
      secondTerm = total
      count += 1
    return total

print(calc_fib(4))    
