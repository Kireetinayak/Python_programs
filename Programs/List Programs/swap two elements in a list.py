mylist=[2,3,4,5,6]
def swap_elements(mylist,pos1,pos2):
    #pos1, pos2=1,3
    mylist[pos1],mylist[pos2]=mylist[pos2],mylist[pos1]
    print(mylist)
swap_elements(mylist,0,3)


def seap2_elements(mylist,in1, in2):
    first=mylist.pop(in1)
    print(first)
    secand=mylist.pop(in2)
    print(secand)

    mylist.insert(mylist[0], secand)
    mylist.insert(mylist[3], first)
    print(mylist)
seap2_elements(mylist,0,3)