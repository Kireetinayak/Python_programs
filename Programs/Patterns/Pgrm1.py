num=(int(input("Enter the number of row :")))
for i in range(1, num+1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()

num=(int(input("Enter the number of row :")))
k=1
for i in range(1, num+1):
    for j in range(1, k+1):
        print("*", end=" ")
    k=k+2
    print()

num=(int(input("Enter the number of row :")))
for i in range(0, num):#0,1,2,3,4
    for j in range(0, num-i-1): # 5-0-1=4
        print(end=" ")
    for j in range(0, i+1):#0+1=1
        print("*", end=" ")
    print()