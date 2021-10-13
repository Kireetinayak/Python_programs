class Demo:
    def __init__(self,a,b):
        self.x=a
        self.y=b

    def addition(self):
       s= self.x+self.y
       print("Addition of X and y is :",s)

    def subtraction(self):
        s = self.x - self.y
        print("Subtraction of X and y is :", s)

Obj=Demo(10,30)
Obj.addition()
Obj.subtraction()

a=(1,2,3)
a=a*2
print(a)
print(type(a))