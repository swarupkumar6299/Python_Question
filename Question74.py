"""
Find words which are greater than given length k
A string is given, and you have to find all the words (substrings separated
by a space) which are greater than the given length k.
Input : str = &quot;hello geeks for geeks
is computer science portal&quot; K=4
"""
str1= input("Enter any string ")
list1=str1.split()
print(list1)
k=int(input("Enter value k:- "))
for word in list1:
    if len(word)>k:
        print(word,end=' ')