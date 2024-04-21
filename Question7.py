#Distance and Time: You're planning a road trip and want to estimate the travel time. Write a program that prompts you for the distance you need to travel and your average driving speed. The program should calculate the estimated travel time in hours (considering potential breaks if desired).
Distance = float(input("Enter the distance you need to travel:- "))
speed = float(input("Enter your average driving soeed:- "))
break_time = int(input("Enter your break time :- "))
Time = (Distance / speed) 
estimate_time = Time + break_time
print(f"Estimate Travel time = {Time :.2f}")
