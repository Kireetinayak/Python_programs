def length_of_list(mylist):
    size=len(mylist)
    print("List size1: ",size)

    count=0
    for i in mylist:
        count=count+1
    print("List of size1: ",count)

    m=0
    for i in range(0,size):
        m=m+1
    print("Size of list3: ",m)

length_of_list(mylist=[2,3,4,5,6,7,8,9,8])
