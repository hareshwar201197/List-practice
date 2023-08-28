# Write a Python function that takes two lists and returns True
# if they have at least one common member.

def validate(lst1,lst2):
    for i in lst1:
        if i in lst2:
            return True
        else:
            return False

v = validate([1,2,3,4], [9,8,7,6,0])
print(v)