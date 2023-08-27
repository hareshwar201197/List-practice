# Small number in list

def small_mun(item):
    small_value = item[0]
    for value in item:
        if small_value > value:
            small_value = value
    return small_value

small_number = small_mun([11,2,3,4,5,5])
print(small_number)