# Write a program to count vowels in input string
str1= input("Enter any string:- ")
c = 0
for ch in str1:
    if ch in "aeiouAEIOU":
        c=c+1
print(f"count oc vowel {c}")