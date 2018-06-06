package in.co.dhrubaray.spark.sql;

import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;
import org.apache.spark.sql.types.DataType;
import org.apache.spark.sql.types.DataTypes;

import static org.apache.spark.sql.functions.col;

public class IplMaxRunSql {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		SparkSession spark = SparkSession
				  .builder()
				  .appName("IPL Max Run")		  
				  .getOrCreate();
		spark.sparkContext().setLogLevel("OFF");
		Dataset<Row> df = spark.read().option("header", "true").csv("matches.csv");
		df.createOrReplaceTempView("ipl");
		spark.sql("SELECT season, max(cast(win_by_runs as int)) FROM ipl group by season order by season").show();
	}

}
