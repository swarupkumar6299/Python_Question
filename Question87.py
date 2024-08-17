'''Maping:- Python support only one mapping collection called dictionary.
In dictionary values are mapped with key
In dictionary data is organized as key and values pair.
This key and values is called items of dictionary.
A key is mapped with one or more than one value.
Dictionary is mutable collection. After creating dictionary changes can be done.
Dictionary key are unique (or )dictionary does not allow duplicate keys but dictionary allow duplicate values.
Dictionarty keys are hashable (immutable objects).Dictionarty keys cannot change but dictionary values can be changed.
In application development dictionary is used to organized data as key and value pair
 '''

dict1 ={}
print(type(dict1))

dict2={'naresh':600,'Suresh':800,'Yash':700,'Hritik':1000}
print(dict2)

list=[(1,10),(2,20),(3,30),(4,40),(5,50)]
print(type(list),list)
d1 =dict(list)
print(d1,type(d1))
e1 = enumerate(list)
print(e1,type(e1))
dict3=dict(e1)
print(dict3,type(dict3))
e = enumerate(list,start =1)
d4 = dict(e)
print(d4, type(d4))

s = [1000,20000,3000,4000,5000]
e = enumerate(s,start = 2001)
sales = dict(e)
print(sales,type(sales))

list1 =[1,2,3,4,5]
list2 = [10,20,30,40,50]
list3 = [(list1[i],list2[i]) for i in range(5)]
print(list3)
#zip() Function

list2 = [1,2,3,4,5,6]
list3 = [10,20,30,40,50,60]
d5 = dict(zip(list2,list3))
print(d5)


d10 = dict(zip("ABC","XYZ"))
print(d10)

d5 = {2010:[1000,2000,3000,4000,5000],
      2011:[5000,6000,7000,8000],
      2012:[4000,12000,16000,2000]}
print(d5,type(d5))

d6 ={'naresh':{'job':'CEO','Salary':6000},'Suresh':{'job':'HR','salary':12000}}
print(d6)