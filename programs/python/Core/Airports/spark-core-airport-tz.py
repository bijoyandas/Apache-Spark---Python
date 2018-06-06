from pyspark import SparkConf,SparkContext

sc=SparkContext(conf=SparkConf().setAppName('Airport timezone'))
mainRdd = sc.pickleFile('airports_mod.pickle')
mainRdd = mainRdd.map(lambda d:(d['Tz'],1))
mainRdd = mainRdd.reduceByKey(lambda acc,b:acc+b)
for item in mainRdd.collect():
	print(item)
