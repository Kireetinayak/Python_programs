with open("text.txt","r")as file:
    for line in file:
       # print(line)
        for word in line.split():
            print(word)