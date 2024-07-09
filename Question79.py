def add(*values):
    s =0
    for value in values:
        s+=value
    return s
res1 = add()
print(res1)
res2 = add(100,200,300)
print(res2)