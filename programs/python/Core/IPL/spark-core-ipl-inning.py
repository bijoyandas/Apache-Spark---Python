from pyspark import SparkConf,SparkContext

sc=SparkContext(conf=SparkConf().setAppName("Innings Run"))

inningData=sc.pickleFile('deliveries.pickle')
inningData=inningData.map(lambda s:((int(s['match_id']),int(s['inning'])),int(s['total_runs']))).reduceByKey(lambda a,b:a+b).sortByKey()
for item in inningData.collect():
	print(item)
