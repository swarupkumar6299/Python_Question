#Write a program to find input string alphabetical string or not 
str1 = input("Enter any string ")
result = True
for ch in str1:
    if(ch>='A' and ch<='Z') or (ch>='a' and ch<='z'):
        pass
    else:
        result =False
        break
print(result)
