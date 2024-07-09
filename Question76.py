#Dictionary Question
"""
Write a program to read sales of n sales persons and display each sales person having 
name and sales.
"""
n = int(input("Enter how many sales person:- "))

#without comprehension

sales = {}
for i in range (n):
    name = input("Enter name ")
    s= float(input("Enter sales "))
    sales[name]=s
print(sales)

# with Comprehension
sales = {input("Enter Name:- "):float(input("Enter Sales:- "))for i in range(n)}
print(sales)