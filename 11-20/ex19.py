
# this is defines the function, parameters and print the statemetns
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


# this will be the first thing that prints, because the function hasn't been called yet
print("We can just give the function numbers directly:")
# first function call
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script:")
# new variables
amount_of_cheese = 10
amount_of_crackers = 50

# 2nd function call with new variables and values
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
# 3rd function call with parameters in equation
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
# 4th function call with variables plus values in an equation
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
