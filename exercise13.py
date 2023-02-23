from sys import argv

script, first, second, third = argv

# didn't realize for awhile, but add arguments in command line
# this is not *args unpacking
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second var is:", second)
print("your third var is:", third)
