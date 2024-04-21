#Unit Converter: Write a program that converts a value between different units (e.g., meters to feet, Celsius to Fahrenheit) based on #the conversion factor entered by the user.
Value = float(input("Enter the value to convert:- "))
Feet = (Value*3.28084)
Fahrenheit =(Value*9/5)+32
print(f"The value of meter to feet is:- {Feet}")
print(f"The value of celsius to Fahrenheit is :- {Fahrenheit}")