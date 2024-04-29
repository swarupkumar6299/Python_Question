#write a program to accept percentage from the user and display the grade according to the following cretia.
"""
Mark                              Grade
>90                                 A
>80 and <= 90                       B
>= 60 and <=80                      C
below 60                            D
"""
mark= int(input("enter your mark:- "))
if mark>90:
    print("A")
if mark>80 and mark<=90:
    print("B")
if mark>=60 and mark<=80:
    print("C")
if mark<60:
    print("D")