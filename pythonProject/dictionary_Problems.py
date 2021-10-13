#Empty Dict
l={}
#Add elements to dict
l["name"]="King"
l["age"]=30
l["Birth_place"]="Goa"
print(l)
#print keys
print(l.keys())
#prints Values
print(l.values())
#Update values
l.update(Birth_place="Bangalore")
print(l)
#pop
l.pop("name")
print(l)
#popitem
l.popitem()
print(l)