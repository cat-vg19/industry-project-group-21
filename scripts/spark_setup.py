"""
spark_setup.py

Shared SparkSession builder.
"""

from pyspark.sql import SparkSession


def get_spark(app_name: str = "bnpl-industry-project",
               driver_memory: str = "6g",
               shuffle_partitions: int = 8) -> SparkSession:
    spark = (
        SparkSession.builder
        .appName(app_name)
        .master("local[*]")
        .config("spark.sql.repl.eagerEval.enabled", True)
        .config("spark.driver.memory", driver_memory)
        .config("spark.sql.shuffle.partitions", str(shuffle_partitions))
        .getOrCreate()
    )
    spark.sparkContext.setLogLevel("ERROR")
    return spark

import warnings

from pyspark.sql import SparkSession


# Suppress PySpark's pandas >= 3.0 compatibility warning.
warnings.filterwarnings(
    "ignore",
    message=r"PySpark does not yet fully support pandas >= 3\.0\.0.*",
    category=FutureWarning,
)