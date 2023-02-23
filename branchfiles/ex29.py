cats = 30
people = 20
dogs = 15

# x += 1 is the same as doing x = x + 1

if people < cats:
    print("Too many cats! The world is doomed!")  # runs
if people > cats:
    print("Not many cats! The world is saved!")
if people < dogs:
    print("The world is drooled on!")
if people > dogs:
    print("The world is dry")  # runs

dogs += 5
if people >= dogs:
    print("People are greater than or equal to dogs")  # runs
if people <= dogs:
    print("People are less than or equal to dogs.")  # runs
if people == dogs:
    print("People are dogs")  # runs
