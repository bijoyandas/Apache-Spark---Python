from pyspark.sql import SparkSession
from pyspark.sql import functions

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL IPL Matches") \
    .getOrCreate()

df = spark.read.option("header", "true").csv("matches.csv")

# Register the DataFrame as a SQL temporary view
df.createOrReplaceTempView("ipl")

sqlDF = spark.sql("select season,max(cast(win_by_runs as int)) FROM ipl group by season order by season")
sqlDF.show()
