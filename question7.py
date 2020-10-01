a,b=map(int,input().split(','))
list=[]
for i in range(a):
    temp=[]
    for j in range(b):
        temp.append(i*j)
    list.append(temp)
print(list)
