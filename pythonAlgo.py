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

original_string = input('Enter a sentence or word ')
print("Original string ", original_string)
#split_string = [*original_string]
size = len(original_string)

print("Printing only even characters")
# for i in range(0, size - 1, 2):
#print("index[", i, "]", original_string[i])

x = list(original_string)
for i in x[0::2]:
    print(i)
