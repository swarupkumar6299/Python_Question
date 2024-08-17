#Login Application

user_dict = {'naresh':'n123',
             'suresh':'s321','Kishore':'k345','ramesh':'r345'}
uname = input("UserName: ")
pwd = input("Pasword: ")

if uname in user_dict:
    password = user_dict[uname]
    if pwd == password:
        print(f'{uname} welcome')
    else:
        print()