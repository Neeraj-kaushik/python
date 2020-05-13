a=[]
b=[] 
for i in range(1,101):
    if i%2==0:
        c=i
        print("even no are",c)
        a.append(c)
    else:
        d=i
        print("odd no are",d)
        b.append(d)
print("list of even no is",a)
print("list of odd no is ",b)