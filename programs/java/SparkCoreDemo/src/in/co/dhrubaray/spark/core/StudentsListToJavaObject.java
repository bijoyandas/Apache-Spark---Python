package in.co.dhrubaray.spark.core;

import java.util.ArrayList;
import java.util.List;

import org.apache.spark.SparkConf;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;

import in.co.dhrubaray.spark.core.beans.Student;

public class StudentsListToJavaObject {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		JavaSparkContext jsc = new JavaSparkContext(new SparkConf().setAppName("Student List to Java Object"));
		
		List<Student> l = new ArrayList<>();
		l.add(new Student(1, "Doug Cutting", "CSE", "HADOOP", 95));
		l.add(new Student(1, "Doug Cutting", "CSE", "SPARK", 85));
		l.add(new Student(1, "Doug Cutting", "CSE", "HDFS", 75));
		l.add(new Student(2, "Matei Zaharia", "CSE", "HADOOP", 90));
		l.add(new Student(2, "Matei Zaharia", "CSE", "SPARK", 96));
		l.add(new Student(2, "Matei Zaharia", "CSE", "HDFS", 76));
		JavaRDD<Student> studentsRdd = jsc.parallelize(l);
		studentsRdd.saveAsObjectFile("students.obj");
	}

}
