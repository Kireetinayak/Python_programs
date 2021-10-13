for i in range(1001):
    digits=len(str(i))
    num=i
    result=0
    while(i!=0):
        rem=i%10
        result=result+rem**digits
        i=i//10
    if num==result:
        print(num)

# Python program to check if the number is an Armstrong number or not

# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
    print(num, "is not an Armstrong number")



