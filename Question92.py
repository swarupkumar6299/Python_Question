#Python program to check whether the string is symmetrical or palindrome
str1 = input("Enter any string ")
if len(str1)%2 == 0:
    i = len(str1)//2
    first =str1[:i]
    second = str1[i:]
    if first == second:
        print("The entered string is symettrical")
    else:
        print("The entered is not symmetrical")
else:
    print("The entered string is not symmetrical")
if str1==str1[::-1]:
    print("The entered string is plaindrome")
else:
    print("The entered string is not palindome")   
