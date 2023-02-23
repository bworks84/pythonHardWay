# Count the number of duplicates


# steps:
# 1. convert string into list
# 2. loop through list
# 3. return f-string in this format ('a' occurs three times)


def duplicate_count(text):
    first = set()
    dup_list = set()

    for i in text:
        i = i.lower()
        if i in first:
            dup_list.add(i)
        else:
            first.add(i)
    return len(dup_list)

# def duplicate_count(text):
#     find_dup = {x for x in text if text.count(x) > 1}
#     return find_dup


print(duplicate_count('batter up'))
