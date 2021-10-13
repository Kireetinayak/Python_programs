# s = '1234567890'
# o = []
# while s:
#     o.append(s[:2])
#     s = s[2:]
# print(o)
# for i in o:
#     print(i)

#x="1234567890"
x="abcdefghijklmnopqrstuvwxyz"
n=2
list=[]
for i in range(0,len(x),n):
    list.append(x[i:i+n])
print(list)