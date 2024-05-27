#logic Application
user = input("UserName: ")
pwd = input("password: ")
if user.strip()=="nit"and pwd.strip()=="n123":
    print("welcome")
else:
    print("invalid username or password")
print("******************************************")
names_list=["ramesh","naresh","kishore","kiran","rajesh","naren"]
for name in names_list:
    if name.endswith("n"):
        print(name)
print("*******************************")
for name in names_list:
    if name.endswith("an"):
        print(name)
print("*******************************************")
for name in names_list:
    if name.endswith(("h","e")):
        print(name)
