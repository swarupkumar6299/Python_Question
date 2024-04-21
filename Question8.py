#Painting a Room: You need to paint a rectangular room. Write a program that calculates the amount of paint needed (in gallons) based on the room's dimensions (length, width, and height) and the paint coverage per gallon.
length = float(input("Enter your room length :- "))
width = float(input("Enter your room width :- "))
Height = float(input("Enter your room height :- "))
requirment_paint = float(input("Enter the paint coverage per gallon:- "))
surface_area = 2*(length * Height + width * Height)
paint_needed = surface_area / requirment_paint 
print(f"The amount of paint needed to paint is: {paint_needed:.2f}")