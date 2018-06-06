"""
Program for calculating highest individual runs by a batsman

"""

from pyspark import SparkConf,SparkContext

sc=SparkContext(conf=SparkConf().setAppName("Batsman Highest"))

batsmanData=sc.pickleFile("deliveries.pickle")
batsmanData=batsmanData.map(lambda s:((int(s['match_id']),s['batsman']),int(s['batsman_runs']))).reduceByKey(lambda a,b:a+b).sortByKey()
batsmanData=batsmanData.map(lambda a:(a[0][1],a[1])).reduceByKey(lambda a,b:a if a>b else b)
for item in batsmanData.collect():
	print(item)
