import pandas as pd
# Series
a=[1,7,5]
my_var= pd.Series(a)
print(my_var)

#DataFrame
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
myvar=pd.DataFrame(mydataset)
print(myvar)

# When using [], the result is a Pandas DataFrame.
#Locate Row
print(myvar.loc[[0,1]])

print(myvar.loc[0])