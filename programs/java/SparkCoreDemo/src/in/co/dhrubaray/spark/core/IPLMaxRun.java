package in.co.dhrubaray.spark.core;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.List;

import org.apache.hadoop.log.LogLevel;
import org.apache.spark.SparkConf;
import org.apache.spark.api.java.JavaPairRDD;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.broadcast.Broadcast;
import org.apache.spark.storage.StorageLevel;

import in.co.dhrubaray.spark.core.beans.Student;
import scala.Tuple2;

public class IPLMaxRun {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		JavaSparkContext jsc = new JavaSparkContext(new SparkConf().setAppName("Student List to Java Object"));
		jsc.setLogLevel("WARN");
		JavaRDD<Map<String, String>> matchesRddDict = jsc.objectFile("matches4.obj");
		matchesRddDict.persist(StorageLevel.MEMORY_ONLY());
		JavaPairRDD<String, Integer> seasonRunRdd = matchesRddDict.mapToPair(
			m -> new Tuple2<>(m.get("season"), Integer.parseInt(m.get("win_by_runs")))
		);
		JavaPairRDD<String, Integer> seasonRunRdd2 = seasonRunRdd.reduceByKey((a, b) -> a > b ? a : b);
		JavaPairRDD<String, Integer> seasonRunRddSorted = seasonRunRdd2.sortByKey();
		for (Tuple2<String, Integer> t : seasonRunRddSorted.collect())
			System.out.printf("%s: %d\n", t._1, t._2.intValue());
	}

}
