from pyspark import SparkConf,SparkContext

sc=SparkContext(conf=SparkConf().setAppName("Sourav App"))
sourav_data=sc.textFile('deliveries.csv')
title_row=sc.broadcast(sourav_data.first().split(','))
print(title_row)
sourav_data=sourav_data.filter(lambda s: not s[:8] == 'match_id')
def strtodict(s):
	i=0
	l=s.split(',')
	d={}
	for key in title_row.value:
		d[key]=l[i]
		i+=1
	return d

sourav_data_dict=sourav_data.map(strtodict)
sourav_data_dict.saveAsPickleFile('deliveries.pickle')
