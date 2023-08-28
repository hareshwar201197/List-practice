
#  Write a Python program to remove duplicates from a list

dup_items = set()
uniq_item = []

a = [10,20,30,20,10,50,60,40,80,50,40]

for i in a:
    if i not in dup_items:
        dup_items.add(i)
        uniq_item.append(i)
print(dup_items)
print(uniq_item)


# lst = [1,2,3,4,2,3,9]
# lst2 = []
#
# for l in lst:
#     if l not in lst2:
#         lst2.append(l)
#
# print(lst2)