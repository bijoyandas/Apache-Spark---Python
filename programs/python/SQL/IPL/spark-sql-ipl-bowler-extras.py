from pyspark.sql import SparkSession

spark=SparkSession.builder.appName("Extra Runs").getOrCreate()

df=spark.read.option("header","true").csv("deliveries.csv")
df=df.select('bowler',(df['wide_runs'].cast('int')+df['bye_runs'].cast('int')+df['legbye_runs'].cast('int')+df['noball_runs'].cast('int')).alias('extras')).groupBy('bowler').sum('extras').orderBy('bowler')
df.show()
