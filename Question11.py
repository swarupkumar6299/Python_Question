#Write a program to find input year leap or not
year = int(input("Enter year"))
print(f"Given year{year} is leap")if year%4==0 or year%400==0 else print(f"Given year {year} in not leap year")