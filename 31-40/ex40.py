# Modules, Classes, and Objects

# Modules are like dictionaries
# 1. Modules are a Python file with some function or variable in it
# 2. You then import that file
# 3. Then you can access teh functions or variables in that module with the   '.' operator


def apple():
    print("I am an apple")

# Can use apple() by importing ex40.apple()


orange = "Living the dream"

# access the same way
# (on a different file...do below)
# import ex40
# ex40.apple()

# Classes -  a class is a way to take a grouping of function and data and place them inside a container so you can access them with the '.' operator.

# Classes are like blueprints for creating new mini-modules. Importing classes is done by instantiating, which is like creating a version of the class. When you instantiate, or create, an a class, what you get is an object


class MyStuff():
    def __init__(self):
        self.orange = "Here's an orange"

    def apple(self):
        print("I'm an apple too")


newObject = MyStuff()
newObject.apple()  # calling this object's function first
print(newObject.orange)  # then printing the object's variable which is a string

# Python recognizes the creation of a class
# Python crafts an empty object with all the functions you've specified in the class using def
# Python then checks if there is an __init__ func and if there is calls that func to initialize your newly created empty object
# In the newObject func __init__ you get new var 'self', which is the empty object Python created and I can set variables on it just like a module, dict, or other object
# In this case I set self.orange to a string and I've initialized the object
# -----------------------------------------------
# When you call a class like a function, Python is using the class as a blueprint for how to build a copy of that type of thing
