from pyspark import SparkConf,SparkContext

sc=SparkContext(conf=SparkConf().setAppName("Bowler Wickets"))

wicketsData=sc.pickleFile("deliveries.pickle")
wicketsData=wicketsData.map(lambda s:(s["bowler"],s["player_dismissed"])).mapValues(lambda a:0 if a=="" else 1).reduceByKey(lambda a,b:a+b).sortByKey()
for item in wicketsData.collect():
	print(item)
