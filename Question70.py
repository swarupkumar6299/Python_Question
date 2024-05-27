name="nit"
print(name.ljust(20,))
print(name.rjust(20,))
print(name.center(20))
print("***********************************************")
stud_list=[["naresh","c"],["suresh","java"],["ramesh","c++"],["kishor","C++"],
           ["kishor","oracal"],["rajesh","mysql"]]
for stud in stud_list:
    print(stud[0].ljust(20),stud[1].ljust(10))
print("**************************************************")
user = input("UserName: ")
pwd = input("Password: ")
if user.lstrip()=="nit" and pwd.lstrip()=="n123":
    print("welcome")
else:
    print("invalid username or password")