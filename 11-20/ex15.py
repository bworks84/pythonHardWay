from sys import argv

script, filename = argv

# open is a built-in method that opens a file specified
txt = open(filename)

# using f strings interpolation
print(f"Here's your file {filename}")
# read method reads the contents of the txt variable from above,
# which is calling the open method on a txt file
print(txt.read())

print("Type the filename again: ")
file_again = input("> ")

# repeats the process
txt_again = open(file_again)

print(txt_again.read())
