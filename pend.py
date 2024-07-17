import pandas as pd

file = pd.read_csv('practice.csv')
df = pd.DataFrame(data=file)
# print(df.columns)


# accenssing months in the dataframe 
print(df['Month'][1])

for i in zip(df['Month'],df['Temperature']):
    print(i)
