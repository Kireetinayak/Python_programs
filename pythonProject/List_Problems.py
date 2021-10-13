#Empty List
s=[]

#append
s.append(2)
s.append(4)
# Insert
s.insert(1,3)
print("s :",s)

#Extend- Add 2 lists
s2=[10,20,30]
print("s2:",s2)
s.extend(s2)
print("s:",s)

#Reverse list
s.reverse()
print("s:",s)

# Sort list
s.sort()
print("s:",s)

#Pop
s.pop()
print("s:",s)

#Remove
s.remove(4)
print("s:",s)