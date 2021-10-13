with open("text.txt","r")as file:
    for i in file:
        for m in i.split():
            for k in m:
                print(k)
file.close()


#     for i in file.readlines():
#         print(i)
#         s=i.split()
#         print(s)
#         for m in s:
#             for r in m:
#              print(r)

