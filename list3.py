
# Largest number from a list

def max_values(item):
    max_value = item[0]
    for value in item:
        if max_value < value:
            max_value = value
    return max_value
maximum_value = max_values([11,21,-151,51,101])
print(maximum_value)

# lst = [11,21,151,51,101]
# max_value = lst[0]
# for value in lst:
#     if max_value < value:
#         max_value = value
#
# print(max_value)