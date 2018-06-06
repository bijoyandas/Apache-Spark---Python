from pyspark import SparkConf,SparkContext

sc = SparkContext(conf=SparkConf().setAppName('Airports City'))
mainRdd = sc.pickleFile('airports_mod.pickle')
mainRdd = mainRdd.map(lambda d:(d['Country'],1))
mainRdd = mainRdd.reduceByKey(lambda acc,b:acc+b)
for item in mainRdd.collect():
	print(item)
