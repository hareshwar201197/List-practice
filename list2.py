
# multiply all the  items in list

def multy(item):
    multi_count = 1
    for value in item:
        multi_count *= value
    return multi_count
total = multy([1,-2,3,4,-5])
print(total)



