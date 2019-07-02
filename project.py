from itertools import islice
from pyspark.sql import functions as f

# sc = SparkContext() # launched automatically in cluster

csv_path = "s3://bakecik/data_gr_A_csv.csv"
task1_path = "s3://bakecik/task1"
task2_path = "s3://bakecik/task2"

# Loading csv file with data to RDD (Resilient Distributed Datasets)
rdd1 = sc.textFile(csv_path).map(lambda line: line.split(","))

# removing the first row as it contains the header
rdd1 = rdd1.mapPartitionsWithIndex(lambda idx, it: islice(it, 1, None) if idx == 0 else it)

# Creating DataFrame from RDD
df1 = rdd1.toDF(["nr", "id", "company", "city", "name"])

# first query
query1 = df1.groupBy(df1.company, df1.city, df1.name).count().where(f.col('count') > 1)
# query1.show()
query1.select("company", "city", "name", "count").write.save(task1_path, format="csv")

# second query
place = 'Cumbernauld'
df2 = df1.crosstab('name', 'city').select('name_city', place)
names = ['Ray', 'Cade', 'Seth']
df2.filter(df2.name_city.rlike('|'.join(names))).write.save(task2_path, format="csv")
