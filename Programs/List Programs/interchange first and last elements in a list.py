mylist=[2,3,4,5,6,7]
#First Approches

# size=len(mylist)
#
# temp=mylist[0]
# mylist[0]=mylist[size-1]
# mylist[size-1]=temp
#
# print("After interchange first and last element: ",mylist)

#Secand Approches
#mylist[0],mylist[-1]=mylist[-1],mylist[0]
#print(mylist)

#3rd approach
start,*middle,end=mylist

mylist=end,*middle,start
print(mylist)