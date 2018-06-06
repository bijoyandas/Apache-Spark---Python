from pyspark.sql import SparkSession
from pyspark.sql import functions

spark = SparkSession.builder.appName("Python Spark SQL IPL Matches").getOrCreate()

df = spark.read.option("header", "true").csv("matches.csv")
df.select('season', df['win_by_runs'].cast('int')).groupBy('season').max('win_by_runs').orderBy('season').show()
