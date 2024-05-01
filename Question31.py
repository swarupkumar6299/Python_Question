# write a program to find input password is valid or invalid.
pswd = input("Enter your  Password:- ") #abcd123$%
ac,dc,sc = 0,0,0
for ch in pswd:
    if (ch>='A' and ch<='Z') or (ch>='a' and ch<='z'):
        ac+=1
    elif (ch>='0' and ch<='9'):
        dc+=1

    else:
        sc+=1
if(ac+dc+sc)>=8:
    if ac>=4 and dc>=2 and sc>=2:
        print("Password is Valid")
    else:
        print("Invalid password must have 4 alphabet, 2 digit and 2 special Character")
else:
        print("length of password must be >=8")    


