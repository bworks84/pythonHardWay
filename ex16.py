from sys import argv

script, filename = argv

# inputting some name of a file below
print(f"We're going to erase {filename}")
print("If you don't want that, hit Control-C")
print("If you do, press Enter")
input("?")

print("Opening file....")
# Open method with a "w" = open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
# '+' (example. 'w+') = Open a file for updating (reading and writing)
target = open(filename, "w")

print("truncating the file. goodbye")
# The truncate() method resizes the file to the given number of bytes.
# If the size is not specified, the current position will be used.
target.truncate()

print("now I'm going to ask you for three lines")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file")

# writes input from user and adds a line break
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it")
target.close()
