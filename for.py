#basic syntax operation 
a=[1,2,3,4]
for b in a:
    print(b)
#operation on tupple
tup=[(1,2),(3,4),(5,6)]
for c in tup:
    print(c)
for x,y in tup:
    print(x)
    print(y)
#operation on dictionary
d={'a':1,'b':2,'c':3}
for e in d:
    print(e)
#to print item from the dictionary
for e in d.items():
    print(e)