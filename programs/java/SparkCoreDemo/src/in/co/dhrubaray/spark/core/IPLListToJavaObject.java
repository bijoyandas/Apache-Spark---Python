package in.co.dhrubaray.spark.core;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.List;

import org.apache.hadoop.log.LogLevel;
import org.apache.spark.SparkConf;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.broadcast.Broadcast;

import in.co.dhrubaray.spark.core.beans.Student;

public class IPLListToJavaObject {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		JavaSparkContext jsc = new JavaSparkContext(new SparkConf().setAppName("Student List to Java Object"));
		jsc.setLogLevel("WARN");
		JavaRDD<String> mainRdd = jsc.textFile("matches.csv");
		Broadcast<String[]> titleRow = jsc.broadcast(mainRdd.first().split(","));
		
		JavaRDD<String> matchesRdd = mainRdd.filter(s -> !s.substring(0, 2).equals("id"));
		System.out.println(matchesRdd.first().split(",").length);
		
		JavaRDD<Map<String, String>> matchesRddDict = matchesRdd.map(s -> {
			String[] l = s.split(",");
			Map<String, String> d = new HashMap<>();
			int i = 0;
			for (String key : titleRow.value())
				if (i < 17)
					d.put(key, l[i++]);
			return d;
		});
		matchesRddDict.saveAsObjectFile("matches4.obj");
		
		System.out.println(titleRow.value().length);
	}

}
