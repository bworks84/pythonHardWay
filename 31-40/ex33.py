i = 0
numbers = []

while i < 10:
    print(f"At the top i is {i}")
    numbers.append(i)

    i += 2
    print(f"Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print('The numbers: ')
for num in numbers:
    print(num)
