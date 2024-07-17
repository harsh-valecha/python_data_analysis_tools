import pandas as pd

file = pd.read_csv('practice.csv')
df = pd.DataFrame(data=file)
# print(df.columns)


# accessing months in the dataframe 
# print(df['Month'][1])

# for i in zip(df['Month'],df['Temperature']):
#     print(i)


# loc to access values 
# print(df.loc[1].iat[1]) # getting 1 row 1st column value

# storing the month and temperatures into list of tuples 
values = list(zip(df.index,df['Month'],df['Temperature']))
print(values[:5]) # first five values






