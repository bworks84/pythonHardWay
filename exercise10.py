
# \t adds tab spacing
tabby_cat = "\tI'm tabbed in."
# \n adds newline break without disrupting string format
persian_cat = "I'm split\non a line"
backslash_cat = "I'm \\ a \\ cat."

# \t tabs in front of string
fat_cat = '''
I'll do a list: 
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)


while True:
    for i in ["/", "-", "|", "\\", "|"]:
        print("%s\r" % i)
    break
