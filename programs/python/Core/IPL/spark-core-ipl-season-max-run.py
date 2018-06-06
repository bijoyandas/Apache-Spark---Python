# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from pyspark import SparkConf, SparkContext

sc = SparkContext(conf = SparkConf().setAppName("My App"))
mainRdd = sc.pickleFile('matches.pickle')
mainRdd.persist()
seasonRunRdd = mainRdd.map(lambda d : (d['season'], int(d['win_by_runs']))).reduceByKey(lambda a, b: a if a > b else b).sortByKey()
print(seasonRunRdd.collect())

