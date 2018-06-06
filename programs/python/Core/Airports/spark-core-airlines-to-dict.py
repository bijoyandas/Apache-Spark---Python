from pyspark import SparkContext,SparkConf

sc=SparkContext(conf=SparkConf().setAppName("Airlines App"))
mainRdd = sc.textFile("airports_mod.dat")
l=['Airport_Id','Name','City','Country','IATA','ICAO','Latitude','Longitude','Altitude','Timezone','DST','Tz']
l=sc.broadcast(l)
def stringtodict(s):
	i=0
	d={}
	k=s.split(',')
	for key in l.value:
		d[key]=k[i]
		i+=1
	return d
mainRddDict = mainRdd.map(stringtodict)
mainRddDict.saveAsPickleFile("airports_mod.pickle")
