print("sequence-name[::] OR sequence-name[:]")
list1=list(range(10,110,10))
print(list1)
list2=list1[::]
print(list2)
list3=list1[:]
print(list3)
print("sequence-name[::step]")
list4=list(range(10,110,10))
print(list4)
list5=list4[::1]#start=0,stop=10,step=1--> 0 1 2 3 4 5 6 7 8 9
print(list5)