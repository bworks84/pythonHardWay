from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line too, but how?
#in_file = open(from_file)
indata = open(from_file).read()

# in_file.read()
# len() is a built in method that returns the number of items in the argument
size_indata = len(indata)

print(f"The input file is {size_indata} bytes long")

file_exist = exists(to_file)
print(f"Does the output file exist? {file_exist}")
print("ready, hit Return to continue, CTRL-C to abort")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done")

out_file.close()
# in_file.close()
