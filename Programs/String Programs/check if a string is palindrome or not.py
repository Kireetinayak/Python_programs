def palindrome(text):

    #s=text[::-1]
    rev = ''.join(reversed(text))
    # w = ""
    # for i in text:
    #     w = w + i
    if rev==text:
        print("Panldrome")
    else:
        print("Not palindrom")


string="madam"
print(palindrome(string))

s=" kMalayalam"
k=""
for i in s:
    k=i+k
if k==s:
    print("Palindrom")
else:
    print("Not Palindrom")