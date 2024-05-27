#Write a program to delete a value from list using delete keyword
list1=[10,20,30,40,50]
print(f"Before Delete list in {list1}")
value = int(input("Enter value to Delete:- "))
if value in list1:
    for i in range(len(list1)):
        if list1[i]==value:
            del list1[i]
            break
    print(f"After Deleting{list1}")
else:
    print("value not exit")