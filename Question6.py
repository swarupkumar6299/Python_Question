#Grocery Shopping: You're at the grocery store and need to calculate the total cost of your items. Write a program that prompts you for the price and quantity of each item, then calculates the subtotal, tax (assuming a fixed rate), and final total.
price1 = float(input("Enter the price of the item 1st:- "))
quantity_1 = int(input("Enter the quantity of the item 1st:- "))
price2 = float(input("Enter the price of item 2nd:- "))
quantity_2 = int(input("Enter the quantity of item 2nd:- "))
subtotal = price1 * quantity_1
subtotal = price2 * quantity_2
tax_rate = 0.08
tax = subtotal * tax_rate
Total = subtotal + tax
print(f"Subtotal:- rs {subtotal:.2f} ")
print(f"Tax: rs {tax:.2f}")
print(f"Total: rs {Total:.2f}")