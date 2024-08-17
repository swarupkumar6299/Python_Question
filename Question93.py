#Write a program to convert string from uppercase to lower case
str1= input("Enter any string ")
str2 = str()
for ch in str1:
    if ch>='A'and ch<='Z':
        str2=str2+chr(ord(ch)+32)
    else:
        str2 =str1+ch
print(str1)
print(str2)