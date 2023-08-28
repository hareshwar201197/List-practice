# Write a Python program to find the list of words that are longer than n
# from a given list of words.

def long_words(n, string):
    word_len = []
    txt = string.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len
print(long_words(3, "The quick brown fox jumps over the lazy dog"))


# lst = ['one', 'two', 'three', 'five', 'six']
# n = 3
# list2 = []
# for i in lst:
#     if len(i) == n:
#         list2.append(i)
# print(list2)
