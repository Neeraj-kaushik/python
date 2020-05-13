a=[234,543,6543,2367,745,8765,4567,6087,1567,111,2398,1632,1008,9800]
b=[123,654,3566,1009,234,4765,2455,8334,2775,5334,7654,234,8765,2343]
four=[]
six=[]
eight=[]
ten=[]
three=[]
five=[]
seven=[]
nine=[]
for i in a:
    if i%4==0:
        four.append(i)
    if i%6==0:
        six.append(i)  
    if i%8==0:
        eight.append(i) 
    if i%10==0:
        ten.append(i)
for i in a:
    if i%3==0:
        three.append(i)
    if i%5==0:
        five.append(i)
    if i%7==0:
        seven.append(i)
    if i%9==0:
        nine.append(i)
for i in b:
    if i%4==0:
        four.append(i)
    if i%6==0:
        six.append(i)  
    if i%8==0:
        eight.append(i) 
    if i%10==0:
        ten.append(i)
for i in b:
    if i%3==0:
        three.append(i)
    if i%5==0:
        five.append(i)
    if i%7==0:
        seven.append(i)
    if i%9==0:
        nine.append(i)
print("list of no divisible by four",four)
print("list of no divisible by six ",six)
print("list of no divisible by eight ",eight)
print("list of no divisible by ten",ten)
print("list of no divisible by three ",three)
print("list of no divisible by five",five)
print("list of no divisible by seven",seven)
print("list of no divisible by nine",nine)
