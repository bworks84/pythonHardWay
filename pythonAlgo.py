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


def remove_chars(string, n):

    print("Your entry is: ", string)
    print(f"You've entered to remove {n} characters from {string}")

    new_str = string[n:]
    return new_str


print(remove_chars("Hello Rob", 2))

# don't forget to print (aka console log the function with the arguments)
