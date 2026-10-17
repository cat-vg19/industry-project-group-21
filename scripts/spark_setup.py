
"""
spark_setup.py

Shared SparkSession builder with quiet startup logs.
"""

import os
import warnings

# Set these BEFORE importing or starting Spark.
os.environ["SPARK_LOCAL_IP"] = "127.0.0.1"
os.environ["PYTHONWARNINGS"] = "ignore"

from pyspark.sql import SparkSession


# Suppress Python warnings.
warnings.filterwarnings("ignore")


def get_spark(
    app_name: str = "bnpl-industry-project",
    driver_memory: str = "6g",
    shuffle_partitions: int = 8,
) -> SparkSession:

    spark = (
        SparkSession.builder
        .appName(app_name)
        .master("local[*]")
        .config("spark.sql.repl.eagerEval.enabled", True)
        .config("spark.driver.memory", driver_memory)
        .config("spark.sql.shuffle.partitions", str(shuffle_partitions))
        # Suppress Spark's JVM logs.
        .config("spark.log.level", "ERROR")
        .config("spark.driver.extraJavaOptions", "-Dlog4j2.level=error")
        .getOrCreate()
    )

    # Reduce Spark and Py4J logging.
    spark.sparkContext.setLogLevel("ERROR")

    # Suppress common startup messages from Spark's Java gateway.
    logger = spark._jvm.org.apache.log4j
    logger.LogManager.getLogger("org").setLevel(
        logger.Level.ERROR
    )
    logger.LogManager.getLogger("akka").setLevel(
        logger.Level.ERROR
    )

    return spark
