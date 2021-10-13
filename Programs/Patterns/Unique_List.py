l=[2,2,3,4,5,4,3,2,5,6,7,6,7,5]
empty_list=[]
s={}
for i in l:
    if i not in empty_list:
        empty_list.append(i)

print(empty_list)

for j in l:
    s[j]=l.count(j)
print(s)

l.sort()
print(l)