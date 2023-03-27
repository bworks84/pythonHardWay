# Doing things with lists

ten_things = "Apples Oranges Pies Garden Bread Dinner Soup"

print("Wait that's not ten things in that list")

stuff = ten_things.split(' ')

more_stuff = ["Day", "Night", "dog", "cat", "dessert", "window"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There's {len(stuff)} items now")

print("There we go ", stuff)

print(stuff[1])
print(stuff[-1])
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
