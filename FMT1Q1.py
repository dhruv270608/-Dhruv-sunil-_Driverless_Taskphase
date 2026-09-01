#Program1
a=int(input("Enter integer: "))
l=[]
for i in range(a):
    l.append(input("Enter string: "))
print(l)
len=len(l)
for j in range(0,len):
    l[j]=l[j].lower()
print(l)
d={}
for x in l:
    for k in x:
        if k not in d:
            d[k]=1
        else:
            d[k]=d[k]+1
    else:
        continue       
print(d)




