from pyspark import SparkContext
# from pyspark.sql.functions import avg, max, min
from pyspark.sql import functions as f

path_to_data = 's3://jwszol-meteo-sample-data/2019-01-10/199607daily.txt'
save_csv_path = "s3://bartosz-bielinski/lab3-data/"

# sc = SparkContext()
# Reading data from bucket
file = sc.textFile(path_to_data)
# Changing format to CSV for easier usage
df = spark.read.option("header", "true").csv(file)

# Saving data to bucket as CSV
df.write.save(save_csv_path, format="csv")


# Demo queries in PySpark

# Finding average value from all maximum temperatures
max_temp_df = df[" Max Temp"]
df.select(f.avg(max_temp_df)).show()

# Find max value in Wind Speed
wind_speed_df = df[" Wind Speed"]
df.select(f.max(wind_speed_df)).show()

# Find min value in Wind Speed
df.select(f.min(wind_speed_df)).show()
