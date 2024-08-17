#Python program to check if a string is plaindrome or not if reverse string is equal to original it is called palindrame
str1 = input("Enter any string:- ")
str2 = str1[::-1]
print(str1,str2)
if str1 == str2:
    print("string is plaindrame")
else:
    print("string in not plaindrame")