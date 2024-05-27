#hash Functio
"""
If we want to add a single element to an existing set, we can use the .add() operation.
It adds the element to the set and returns 'None'.
"""
N= int(input())
A=set()

for i in range(N):
    country=input()
    A.add(country)
print(len(A))