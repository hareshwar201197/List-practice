# Write a Python program to count the number of strings from a given list of strings.
# The string length is 2 or more and the first and last characters are the same.
# Sample List : ['abc', 'xyz', 'aba', '1221']

def validate(item):
    count = 0
    for string in item:
        if string[0] == string[-1]:
            count +=1
    return count

string_count = validate(['abc', 'xyz', 'aba', '1221'])
print(string_count)