# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

Author: Dhruba Ray
"""

from pyspark import SparkConf, SparkContext

sc = SparkContext(conf = SparkConf().setAppName("My App"))
mainRdd = sc.textFile('matches.csv')
titleRow = sc.broadcast(mainRdd.first().split(','))
print(titleRow)
matchesRdd = mainRdd.filter(lambda s: not s[:2] == 'id')
print(matchesRdd.take(2))
def stringToDict(s):
	l = s.split(',')
	d = {}
	i = 0
	for key in titleRow.value:
		d[key] = l[i]
		i += 1
	return d
matchesRddDict = matchesRdd.map(stringToDict)
print(matchesRddDict.take(5))
matchesRddDict.saveAsPickleFile('matches.pickle')

