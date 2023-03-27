from sys import argv

script, input_file = argv


def print_all(f):
    print(f.read())

# resets the current position of code to be read to index 0


def rewind(f):
    f.seek(0)

# This function is given two arguments in variable form that it will print
# we don't know the value of either variable yet


def print_a_line(line_count, f):
    print(line_count, f.readline())


# opens input file and stores as variable current_file
current_file = open(input_file)

# start
print("First let's print the whole file: \n")
# next line to process, prints text within input file given on command line (test.txt)
print_all(current_file)
# third line
print("Now let's rewind, kind of a like a tape")

# resets code reader
rewind(current_file)

print("Let's print three lines:")
# gives current_line a value of 1
current_line = 1
# print_a_line takes in current_line variable, which is a number, in this case 1
# current_file references line 21, and is a variable input for the original
# function's argument of readline method which returns one line from the file
# so this first call should return a number of 1, and the text on line one of the input file
print_a_line(current_line, current_file)

# current line now has value of 2
current_line += 1
# this call should return 2 with the text on line two of the input file
print_a_line(current_line, current_file)

# current_line now has value of 3
current_line += 1
# 3 with text from line 3 of input file
print_a_line(current_line, current_file)
