h=[]
n= int(input("enter the size of list"))
for i in range(0,n):
    print("enter the element in list at location ",i ,":")
    c=int(input())
    h.append(c)
print("your list is ",h)
a=int(input("enter the element you want to search"))
h.pop(a)
print("element deleted succesfully")
print("your new list is ",h)
