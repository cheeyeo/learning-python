"""
Example of using for loops
"""

print __doc__

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']


for number in the_count:
  print "This is cound %d" % number

# same as above

for fruit in fruits:
  print "A fruit of type: %s" % fruit


for i in change:
  print "I got %r" % i

elements = []

for i in range(0,6):
  print "Adding %d to the list" % i
  elements.append(i)

for i in elements:
  print "Element was %d" % i

# can directly assign to list from range!

elements2 = range(0,6)
for i in elements2:
  print "Element2 was %d" % i

