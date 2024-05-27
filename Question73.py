"""
Program to check if a string contains any special character
Given a string, the task is to check if that string contains any special
character (defined special character set). If any special character is found,
don’t accept that string.
"""
str1= input("Enter any string:- ")
sp="$%!@#^&"
found=False
for ch in str1:
    if ch in sp:
        found=True
        break
if found:
    print("String is not accepted.....")
else:
    print("String is accepted....") 