def reverse_list(mylist):
    print("Original List: ",mylist)

    #mylist.reverse()

    #newlist=mylist[::-1]
    new=[]
    for i in reversed(mylist):
        #print(i, end=" ")
        new.append(i)
    print(new)

    print("After reverse the list: ",mylist)
reverse_list(mylist=[2,3,4,5,6,7])

#Without method
# Example input list of numbers
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Function takes a list as input
def Reverse(numbers):
    # Base case when the list is only one item
    if (len(numbers) == 1):
        return numbers
    # Otherwise
    return Reverse(numbers[1:]) + numbers[0:1]


# Test function
print(Reverse(numbers))