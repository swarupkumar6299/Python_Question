#Write a program to read sale of M sale person N sale
M = int(input("Enter how many sales person:- "))
N = int(input("Enter how many sales? "))
sales = []
for i in range (M):
    row = []
    for j in range(N):
        s= int(input("Enter sales:- "))
        row.append(s)
    sales.append(row)
print(sales)
