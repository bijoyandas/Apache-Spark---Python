package in.co.dhrubaray.spark.sql;

import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;
import org.apache.spark.sql.types.DataType;
import org.apache.spark.sql.types.DataTypes;

import static org.apache.spark.sql.functions.col;

public class IplMaxRun {

	public static void main(String[] args) {
		SparkSession spark = SparkSession
				  .builder()
				  .appName("IPL Max Run")				  
				  .getOrCreate();
		spark.sparkContext().setLogLevel("OFF");
		Dataset<Row> df = spark.read().option("header", "true").csv("matches.csv");
		df.select(col("season"), col("win_by_runs").cast(DataTypes.IntegerType))
		.groupBy("season").max("win_by_runs").orderBy("season").show();
	}

}
