from pyspark.sql import SparkSession

spark=SparkSession.builder.appName("Batsman Highest App").getOrCreate()

df = spark.read.option("header","true").csv("deliveries.csv")
df = df.select('match_id','batsman',df['batsman_runs'].cast('int').alias('runs')).groupBy('match_id','batsman').sum('runs').orderBy('match_id').select('batsman','sum(runs)').groupBy('batsman').max('sum(runs)').orderBy('batsman').show()
