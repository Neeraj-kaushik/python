a=[]

for b in range(1,101):
    if b > 1:
        for i in range (2,b):
            if (b%i)==0:
                break
    else:
                a.append(b)
    
print("and the no are",a)

