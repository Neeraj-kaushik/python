a=1
c=1
e=0
sum=0
b=input("enter your choice")
while b!="q":
    d=int(input("enter the no"))
    c=c*d
    sum= sum+d
    e=e+1
    b=input("enter your choice")
print("the multiplication of no is ",c)
f=sum/e
print("average is",f)