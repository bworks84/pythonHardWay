import re

# 1


def product_or_sum(number1, number2):
    product = number1 * number2
    if product <= 1000:
        return product
    else:
        return number1 + number2


result = product_or_sum(40, 30)

#print("The result is", result)

# 2
previous_num = 0
for x in range(1, 11):
    sum = x + previous_num
    #print("Current number ", x, "Previous number ", previous_num, " Sum: ", sum)
    previous_num = x

# 3 Print characters from string that are at even index number

#original_string = input('Enter a sentence or word ')
#print("Original string ", original_string)
#split_string = [*original_string]
#size = len(original_string)

#print("Printing only even characters")
# for i in range(0, size - 1, 2):
#print("index[", i, "]", original_string[i])

#x = list(original_string)
# for i in x[0::2]:
# print(i)

# 4 Remove first n characters from a string
# ex remove_chars("pynative", 4)

#enter_str = input("Enter a word or sentence: ")
#n = input("Enter a number of characters you would like to remove: ")


# def remove_chars(string, n):

#     print("Your entry is: ", string)
#     print(f"You've entered to remove {n} characters from {string}")

#     new_str = string[n:]
#     return new_str


# print(remove_chars("Hello Rob", 2))

# don't forget to print (aka console log the function with the arguments)

# 5 Check if first and last character are the same

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 55, 75, 30]


# def check_nums(num_array):
#     # here's how to get the first element in a list
#     # print(num_array[0])
#     # here's one way to get the last element from the same list
#     # print(num_array[-1])

#     if num_array[0] == num_array[-1]:
#         return True
#     else:
#         return False


# print(check_nums(numbers_x))
# print(check_nums(numbers_y))


# 6 Display numbers divisible by 5 from a list

# num_list1 = [1, 20, 3, 7, 5, 10, 6, 18]
# num_list2 = [10, 13, 25, 32, 4, 5, 20]


# def my_func(num_array):
#     div_by_five = []
#     for x in num_array:
#         if x % 5 == 0:
#             div_by_five.append(x)

#     print(div_by_five)


# my_func(num_list1)
# my_func(num_list2)


# 7 Return the count of a given substring from a string

str_x = "Mowglie is a good dog. Mowglie likes treats, naps, and long walks. Mowglie chases lizards"

# search() finds first occurrence
# findall(<pattern>, <string>) finds all occurrences ..... (import re library)


def find_substrings(my_str):
    # find substring exists
    # print("Mowglie" in str_x) # True

    # str_list = my_str.split(' ')  # split to be able to search string
    # print(str_list)
    # just looking for the count of occurrences
    print(
        f"The substring Mowglie occurs {my_str.count('Mowglie')} times in the string")


find_substrings(str_x)
