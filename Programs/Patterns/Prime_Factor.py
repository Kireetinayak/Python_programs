num=int(input("Enter the number: "))
i=2
while(num!=1):
    rem=num%i
    if(rem==0):
        num=num/i
        print(i)
    else:
        i=i+1
