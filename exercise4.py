# this creates a variable with the name of cars and the value of 100
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
# this creates a variable with 2 other variables in an equation
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = round(cars_driven * space_in_a_car)
average_passengers_per_car = round(passengers / cars_driven)

print("There are", cars, "cars available")
print("There are only", drivers, "drivers available")
print("There will be", cars_not_driven, "empty cars today")
print("We can transport", carpool_capacity, "people today")
print("we have", passengers, "to carpool today")
print("We need to put about", average_passengers_per_car, "in each car")
