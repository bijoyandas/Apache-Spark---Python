from pyspark.sql import SparkSession

spark=SparkSession.builder.appName("Batsman Total Runs").getOrCreate()

df=spark.read.option("header","true").csv("deliveries.csv")
df.select('batsman',df['batsman_runs'].cast('int')).groupBy('batsman').sum('batsman_runs').orderBy('batsman').show()
