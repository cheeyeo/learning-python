from sys import argv

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

with open(from_file, 'r') as f:
  indata = f.read()
  print "The input file is %d bytes long" % len(indata)
  out_file = open(to_file, 'w')
  out_file.write(indata)
  out_file.close()

print out_file.closed
