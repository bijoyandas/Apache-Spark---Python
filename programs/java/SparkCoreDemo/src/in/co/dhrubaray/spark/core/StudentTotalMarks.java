package in.co.dhrubaray.spark.core;

import org.apache.spark.SparkConf;
import org.apache.spark.api.java.JavaPairRDD;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.storage.StorageLevel;

import in.co.dhrubaray.spark.core.beans.Student;
import scala.Tuple2;

public class StudentTotalMarks {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		JavaSparkContext jsc = new JavaSparkContext(new SparkConf().setAppName("Student Total Marks"));
		
		JavaRDD<Student> studentsRdd = jsc.objectFile("students.obj");
		studentsRdd.persist(StorageLevel.MEMORY_ONLY());
		JavaPairRDD<String, Integer> studentsPairRdd = studentsRdd.mapToPair(s -> new Tuple2<String, Integer>(s.getName(), s.getMarks()));
		JavaPairRDD<String, Integer> marksRdd = studentsPairRdd.reduceByKey((a, b) -> {return a + b; });
		for (Tuple2<String, Integer> record : marksRdd.collect())
			System.out.format("%s has got %d\n", record._1, record._2);
	}

}
