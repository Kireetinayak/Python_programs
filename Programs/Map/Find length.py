#The map() function applies a given function to each item of an iterable

def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))

print((list(x)))


def myfunc(a, b):
  return a + b

x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
print(list(x))

def myfunc(n):

  return n.count("k")

x = map(myfunc, "aabcdefghijklmnopqrstuvwxyz")
print(list(x))