from pyspark.sql import SparkSession

spark= SparkSession.builder\
.appName("Spark")\
.getOrCreate()

data=[
    ("server1",56),
    ("server2",56),
    ("server3",56),
    ("server4",56),
    ("server5",56),
    ("server6",56),
    ("server7",56),
    ("server8",56),
]
column=["Server Nmae","Cpu usage"]
df=spark.CreateDataFrame(data,column)

df.show()