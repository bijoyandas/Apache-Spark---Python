#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 23:50:23 2017

@author: dray
"""

from pyspark import SparkConf, SparkContext
from pprint import pprint

sc = SparkContext(conf = SparkConf().setAppName("Students read"))
marksRdd = sc.pickleFile("students.pickle").map(lambda d: (d['sid'], d['marks'])).reduceByKey(lambda a, b: a + b).sortByKey()
pprint(marksRdd.collect())
