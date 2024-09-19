#Finding the prime factors
def PFact(num):
  fact = []
  div = 2
  while div <= num:
    if num % div == 0:
      fact.append(div)
      num = num // div
    else:
      div += 1
    return fact
