"""
Example of using while loops in a function
"""

print __doc__

def while_list_incrementor(numbers2, limit2, increment2):
  i=0
  while i < limit2:
    print "At the top i is %d" % i
    numbers2.append(i)

    i+= int(increment2)

    print "Numbers now: ", numbers2
    print "At the bottom i is %d" % i

  return numbers2

def for_list_incrementor(numbers):
  for i in range(0,9):
    print "At the top i is %d" % i
    numbers.append(i)

    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i


numbers = []
limit = 6
increment = 1

while_list_incrementor(numbers, limit, increment)

print "The numbers: "
for num in numbers:
  print num

print "Using incrementor with for loop"
for_list_incrementor(numbers)

print "The numbers: "
for num in numbers:
  print num


