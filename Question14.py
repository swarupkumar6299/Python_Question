#write a program to calculate the electric bill(accept no. of unit from user) according to following catera:-
"""
Unit                                                                             price
First 100 units                                                                no charge
next 100 units                                                                 Rs 5 per units.
After 200 units                                                                Rs 10 per units.
(for example if input unit is 350 than total bill amount is rs 1200)
"""
amount = 0
num = int(input("Enter number electric:- "))
if num<=100:
    print(f"{num} is no charge")
if num>100 and num<=200:
    amount=(num-100)*5
    print (f"{num} is charged bill {amount}")
if num>200:
    amount=500+(num-200)*10
    print(f"{num} is charged bill {amount} ")
    