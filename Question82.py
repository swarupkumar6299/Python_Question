'''Functool.reduce(function, iterable [initializer])
Apply function of two arguments cumulatively to the items of iterable from left to right, so as to reduce (lambda x,y: x+y,[1,2,3,4,5]) calculate ((((1+2)+3)+4)+5). The left argument,x, is the accumulative value and the right argument,y, is the '''

import functools

list1=list(range(10,110,10))
print(list1)
res1= functools.reduce(lambda x,y:x+y,list1)
print(res1)
res2=functools.reduce(lambda x,y:x+y,list1,100)
print(res2)

list2=[]
res3=functools.reduce(lambda x,y:x+y,list2,10)
print(res3)

res4=functools.reduce(lambda x,y:x if x>y else y,list1)
print(res4)
res5=functools.reduce(lambda x,y:x if x<y else y,list1)
print(res5)
res6=functools.reduce(lambda x,y:str(x)+","+str(y),list1)
print(res6,type(res6))
