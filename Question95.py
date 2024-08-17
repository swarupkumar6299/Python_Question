#Python count the number of matching character in a pair of string
str1 = input("Enter first string ")
str2 = input("Enter second string ")
str3 = str()

for ch  in str1:
    if ch not in str3:
        str3=str3+ch
for ch in str3:
    c = str2.count(ch)
    if c>0:
        print(ch,end='')