import time

def times(function):
    def time_cal(*args, **kwargs):
        a=12
        b=23
        c=a+b
        return c

    return time_cal

@times
def program1(number):
    d=15
    v=d+c
    return result
@times
def program2(number):
    result = []
    for i in number:
        result.append(number * number * number)
    return result

array1 = range(1,10)
out_squre = program1(array1)
out_cube = program2(array1)
#print(out_squre)
#print(out_cube)