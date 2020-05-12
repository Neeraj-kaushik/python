#this is program to call document in python
#to open a text file 
x=open('text.txt')
#to read a file and print it
a=x.read()
print(a)
#to read the file again we have to seek the file
x.seek(0)
b=x.read()
print(b)
x.seek(0)
#another way of opening a file
with open('text.txt')as neeraj:
    g=neeraj.read()
print(g)