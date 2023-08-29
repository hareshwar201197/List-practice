#  Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color1 = []

for index, x in enumerate(color):
    if index not in (0,4,5):
        color1.append(x)
print(color1)
# color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]