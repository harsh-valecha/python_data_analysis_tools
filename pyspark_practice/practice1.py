from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('test1').getOrCreate()

df = spark.read.csv('business-operations-survey-2022-price-and-wage-setting.csv',header=True)
print(df.show(5,0)) # gives the first 5 rows

print(df.columns)
print(type(df))