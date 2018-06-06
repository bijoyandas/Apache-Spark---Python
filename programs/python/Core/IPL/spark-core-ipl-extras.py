from pyspark import SparkContext,SparkConf

sc=SparkContext(conf=SparkConf().setAppName("Extra Runs"))
iplData=sc.pickleFile('deliveries.pickle')
iplData=iplData.map(lambda d:(d['bowling_team'],int(d['wide_runs'])+int(d['bye_runs'])+int(d['legbye_runs'])+int(d['noball_runs']))).reduceByKey(lambda a,b:a+b)
for item in iplData.collect():
	print(item)
