test_string = "There 1 are 2 apples for 4 persons"
res = [int(i) for i in test_string.split() if i.isdigit()]
print(res)

