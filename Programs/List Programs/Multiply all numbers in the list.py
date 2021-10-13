def multiply_list_elements(mylist):
    mul=1
    for i in mylist:
        mul=mul*i
    return mul
list1=[2,3]
list2=[12,13,14,15,16,17]
print(multiply_list_elements(list1))
print(multiply_list_elements(list2))
