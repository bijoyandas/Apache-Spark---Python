from pyspark import SparkConf,SparkContext

sc=SparkContext(conf=SparkConf().setAppName("Bowler Extras"))

bowlerData=sc.pickleFile('deliveries.pickle')
bowlerData=bowlerData.map(lambda s:(s['bowler'],int(s['wide_runs'])+int(s['bye_runs'])+int(s['legbye_runs'])+int(s['noball_runs']))).reduceByKey(lambda a,b:a+b).sortByKey()
for item in bowlerData.collect():
	print(item)
