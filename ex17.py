from sys import argv
from os.path import exists # use to test if the file exists

script, from_file, to_file = argv

print(("Copying from %s to %s ") % (from_file, to_file))

# we could do these two on one line, how?
#in_file = open(from_file)
#indata = in_file.read()
indata = open(from_file,"r")

print(("The input file is %d bytes long") % len(str(indata)))

print(("Does the output file exist? %r") % exists(to_file)) # see if the to_file exists
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(str(indata))

print("Alright, all done.")

out_file.close()
indata.close()
