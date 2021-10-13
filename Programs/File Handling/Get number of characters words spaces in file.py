file=open("text.txt","r")
num_words = 0
num_lines = 0
num_charc = 0
num_spaces = 0

for line in file:
    num_lines+=1

    word = 'Y'
    for letter in line:
        if (letter != ' ' and word == 'Y'):
            num_words += 1
            word = 'N'
        elif (letter == ' '):
            num_spaces += 1
            word = 'Y'
            for i in letter:
                if (i != " " and i != "\n"):
                    num_charc += 1
print("Number of words in text file: ", num_words)

# printing total line count
print("Number of lines in text file: ", num_lines)

# printing total character count
print('Number of characters in text file: ', num_charc)

# printing total space count
print('Number of spaces in text file: ', num_spaces)