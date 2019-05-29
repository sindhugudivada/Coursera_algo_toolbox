def max_pairwise_product(numbers):
  firstMax = max(numbers)
  firstMaxIndex = numbers.index(firstMax)
  numbers[firstMaxIndex] = numbers[0]
  numbers[0] = firstMax
  secondMax = max(numbers[1:])
  return secondMax * firstMax
  

print(max_pairwise_product([1,2,3,4,5]))   

