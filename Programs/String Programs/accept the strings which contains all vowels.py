s="ABeeIghiObhkUul"
k=s.lower()
vowels="aeiou"
#m=vowels.split()
#print(m)
m=""
for i in k:
    if i in vowels:
        m=m+i
print(m)
j=" "
for b in m:
    if b not in j:
        j=j+b
print(j)
if vowels in j:
        print("Accepted")
else:
        print("Not Accepted")
