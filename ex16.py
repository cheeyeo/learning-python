from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

# if the file is already opened with 'w' it will overwrite the contents so calling truncate here is redundant
# print "Truncating the file"
# target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
data = "%s\n%s\n%s\n" % (line1,line2,line3)
target.write(data)

print "And finally, we close it."
target.close()



