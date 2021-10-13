test_str = 'Gfg is best . Geeks are good and Geeks like Gfg'

#count1=test_str.split()
#print(count1)
res = {key: test_str.count(key) for key in test_str.split(test_str)}
print(res)