from pyspark.sql import SparkSession


def init_spark(app_name="SAZ Spark App"):
    """Initialize or retrieve a SparkSession."""
    return SparkSession.builder.appName(app_name).getOrCreate()


def spark_schema(df_spark):
    """Print the schema of a Spark DataFrame."""
    df_spark.printSchema()


def spark_cardinality(df_spark):
    """Display value counts for each column in a Spark DataFrame."""
    for col_name in df_spark.columns:
        print(f"Cardinality of {col_name}:")
        df_spark.groupBy(col_name).count().show()


def spark_save_csv(df_spark, path, mode="overwrite"):
    """Save a Spark DataFrame as CSV."""
    df_spark.write.mode(mode).option("header", True).csv(path)
