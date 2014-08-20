from sys import argv

def print_all_args(*args):
  print "args are: %r" % (args)

def print_two(arg1, arg2):
  print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
  print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
  print "I got nothin'."

print_all_args(argv)
print_two("Zed","Shaw")
print_one("First!")
print_none()
