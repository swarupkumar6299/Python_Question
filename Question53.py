#Write a program to find sum, mean, median of given list of values
list1=[4, 5, 8, 9, 10, 17]
sum=0
mean=0
median=0

for i in range(len(list1)):
    sum=sum+list1[i]
    mean=mean+list1[i]/2
    
print(f"Given list of sum is {sum}")
print(f"Given list of mean is {mean}")
print(median)
