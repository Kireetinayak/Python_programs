l=[2,3,4,5,6,7]
k=[]
for i in l:
    k.append(i)
print(k)

print(l[-1::-1])
shift=3
for i in range(0,shift):
    temp=l[0]

    for j in range(0,len(l)-1):
        l[j]=l[j+1]
    l[len(l)-1]= temp

for i in range(0,len(l)):
    print(l[i], end=" ")

