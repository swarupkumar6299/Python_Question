#Write a program to accept the cost of price of a bike and display the road tax to be paid according to the following cretia:-
"""
Cost price (in rs)                     Tax
100000                                  15%
50000 and <= 10000                      10%
<= 50000                                5%
"""
tax=0
cost = int(input("Enter your bike cost"))
if cost > 100000:
    tax =   15/100*cost
elif cost>50000 and cost<=100000:
    tax= 10/100*cost
else:
    tax = 5/100*cost
print(f"Tax to paid {tax}")
