#BMI Calculator: Write a program that calculates the Body Mass Index (BMI) of a person given their weight (in kilograms) and height (in meters) entered by the user. Use the formula BMI = weight / (height * height).
weight = float(input("Enter your weight(in kilogram):- "))
height = float(input("enter your height(in meter):- "))
BMI = weight/(height*height)
print(f"The body mass of index of person given their weight {weight} and height {height} is :- {BMI}")
