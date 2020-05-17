a=[13,4,15.77,55.88,43,66.7,55.77,'neeraj','kaushik','rohit']
b=[]
c=[]
d=[]
for i in a:
    if isinstance(i,int):
            b.append(i)
    if isinstance(i,float):
        c.append(i)
    if isinstance(i,str):
        d.append(i)
print(b)
print(c)
print(d)
