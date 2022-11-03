#Challenge 1
'''
def sum_to(n):
  total = 0
  for num in range(n+1):
    total += num
  return total

print(sum_to(10))
'''



#Challenge 2
'''
def largest(list):
  biggest = 0
  for item in list:
    if item > biggest:
      biggest = item
  return biggest

print(largest([10, 4, 2, 231, 91, 534]))
'''


#Challenge 3
'''
'''
def occurrences(str1, str2):
  list = str1.split(str2)
  return len(list) - 1

print(occurrences('hello, lol. la lala.', 'l'))