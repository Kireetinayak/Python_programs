n=[[10,20,30],[30,20,10],[20,10,30]]
print(n)
l=len(n)
print(l)
for i in n:
    print(i)
for j in range(l):
    for m in range(l[j]):
        print(n[j][m],end=" ")
    print()
