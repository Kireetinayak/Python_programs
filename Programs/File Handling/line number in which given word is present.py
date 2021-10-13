file=open("text.txt")
text="python"
count=1
s=" "
while(s):
    s=file.readline()
    if text in s:
        print("test present ",count)
    count+=1

