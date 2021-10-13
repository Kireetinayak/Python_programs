test_dict = {'gfg' : [5, 6, 7, 8],
             'is' : [10, 11, 7, 5],
             'best' : [6, 12, 10, 8],
             'for' : [1, 2, 5]}
#count=1
k=[]
s=[]
for i in test_dict.values():
    print(i)
    s.extend(i)
print(s)
for m in s:
    if m not in k:
        k.append(m)
    #count+=1

print(k)
k.sort()
print(k)
print(max(k))
print(min(k))
