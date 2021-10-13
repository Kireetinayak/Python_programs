file=open("text.txt","r")
text="selenium, selenium is"
s=" "
count=1
while(s):
    s=file.readline()
   # print(s)
    if text in s:
        print("Text is present in Line Number: ",count)
    count+=1

# k=1
# m=file.readlines()
# print(m)
# for i in m:
#     l=i.split()
#     if text in l:
#         print("Element present",k)
#     k+=1



