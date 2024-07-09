"""
Creat even number sqr  dictionary
"""
Even_dict = {num:num**2 for num in range(1,21)if num%2==0}
print(Even_dict)
Odd_dict = {num:num**2 for num in range (1,21)if num%2!=0}
print(Odd_dict)
"""
Filteration Sales based on condition
"""
sales = {2000:45000,
         }