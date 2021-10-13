def small_element_in_list(mylist):
    #minelement=min(mylist)
    #return minelement

    #maxelement=max(mylist)
    #return maxelement

    mylist.sort()
  #  print(mylist),
   # return (mylist[0])
    return (mylist[-1])



list1=[1,3,2,4,6,5]
list2=[2,4,3,6,12]
print(small_element_in_list(list1))
print(small_element_in_list(list2))