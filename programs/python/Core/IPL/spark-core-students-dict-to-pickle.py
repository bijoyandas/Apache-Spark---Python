# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from pyspark import SparkConf, SparkContext

#kwargs: conf
sc = SparkContext(conf = SparkConf().setAppName("Students insert"))

dataSet = [
        {"sid": 1, "name": "ram sharma", "dep": "it", "sub": "phy", "marks": 56},
        {"sid": 1, "name": "ram sharma", "dep": "it", "sub": "chem", "marks": 75},
        {"sid": 1, "name": "ram sharma", "dep": "it", "sub": "math", "marks": 55},
        {"sid": 2, "name": "sam sharma", "dep": "it", "sub": "phy", "marks": 87},
        {"sid": 2, "name": "sam sharma", "dep": "it", "sub": "chem", "marks": 59},
        {"sid": 2, "name": "sam sharma", "dep": "it", "sub": "math", "marks": 67}
]
rdd = sc.parallelize(dataSet)
rdd.saveAsPickleFile("students.pickle")
