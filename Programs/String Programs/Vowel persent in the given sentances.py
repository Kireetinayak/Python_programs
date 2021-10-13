s="Python is good programing langauge"
v=["a","e","i","o","u"]
f=[]
k=s.lower()
for i in k:
    if i in v:
        print(i)

        if i not in f:
            f.append(i)
print("Count of a: ",k.count("o"))
print(f)