from pyspark.sql import SparkSession

def run_spark_etl():
    spark = SparkSession.builder.appName("HealthMLOpsX_ETL").getOrCreate()
    
    data = [
        {"patient_id": 1, "bmi": 22.5},
        {"patient_id": 2, "bmi": 28.7}
    ]
    df = spark.createDataFrame(data)
    
    df = df.withColumn("risk", df["bmi"] > 25)
    
    # Show or write to S3 / BigQuery / Blob etc.
    df.show()
    
    return {"status": "Spark ETL completed"}
