def reverse_the_word(sentence):

    word=sentence.split(" ")
    print(word)
    new=word[::-1]
    print(new)
    latest=" ".join(reversed(word))
    print(latest)

s="geeks quiz practice code"
reverse_the_word(s)