num=(lambda x:x*2)
print(num(5))

num1=(lambda x,y:x*2+y)
print(num1(5,4))

# Python 3 code to people above 18 yrs
ages = [13, 90, 17, 59, 21, 60, 5]
adults=list(filter(lambda age:age<18,ages))
print(adults)

#Even number
list_1 = [1,2,3,4,5,6,7,8,9]
number=list(filter(lambda num : num%2==0 ,list_1))
print(number)
#map
number1=list(map(lambda nu:nu*3,list_1))
print(number1)