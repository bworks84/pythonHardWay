the_count = [1, 2, 3, 4, 5]
fruits = ["apples", "oranges", "pears", "apricots"]
change = [1, "pennies", 2, "dimes", 3, "quarters"]

for number in the_count:
    print(f"this is {number}")  # prints "This is 1-5"

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")  # prints A fruit of type: {fruits}

# also we can go through mixed lists too
# notice we have to use %r since we don't know whats in it
for i in change:
    print(f"I got {i}")  # same with this loop, prints out each element

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print(f"Add {i} to the list.")  # prints "Add 0-5 to the list"
    # append is a function that lists understand
    elements.append(i)  # appends it to the elements list

# now we can print them out too
for i in elements:
    print(f"Element was: {i}")  # prints out each element added from loop above
