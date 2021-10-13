test_dict = {"Arushi" : 22, "Anuradha" : 21, "Mani" : 21, "Haritha" : 21}
print(test_dict)
del test_dict["Mani"]
#print(remov_value)
print(test_dict)

remove=test_dict.pop("Haritha")
print(test_dict)
print(remove)