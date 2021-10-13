file=open("text.txt")
text="python selenium"
count=1
k=[]
for i in file:
    #print(i)
    if text in i:
        print("text prsesnt in line :",count)
        k.append(count)
    count+=1
print(k)
c=0
for i  in  k :
  c=c+1
print("number of count in file:", c)
print("Number of line presesnt in the file is : ",count-1)