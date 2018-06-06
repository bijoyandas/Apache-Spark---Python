from pyspark import SparkContext,SparkConf

sc=SparkContext(conf=SparkConf().setAppName("Batsman Runs"))

batsmanData=sc.pickleFile("deliveries.pickle")
batsmanData=batsmanData.map(lambda s:(s['batsman'],int(s['batsman_runs']))).reduceByKey(lambda a,b:a+b).sortByKey()
for item in batsmanData.collect():
	print(item)
