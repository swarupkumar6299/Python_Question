#Write a program to count even and odd number of given list
list1=[5,7,6,5,8,2,0,2,4,8]
even_count = 0
Odd_count = 0
for i in range(len(list1)):
    if list1[i]%2==0:
        even_count=even_count+1
    elif list1[i]%2==1:
        Odd_count=Odd_count+1
    else:
        pass
print(f"given list even number is {even_count}")
print(f"Given list odd number ia {Odd_count}")

