-- In Hadoop:

-- Download data from s3
aws s3 cp s3://jwszol-meteo-sample-data/ . --recursive

hadoop fs -mkdir /data/
hadoop fs -put * /data/
hadoop fs -ls /data/


-- In Hive:

-- create table
CREATE EXTERNAL TABLE 165430_ing_m_lab3 ( Wban_Number STRING, YearMonthDay STRING, MaxTemp STRING, MinTemp STRING,
AvgTemp STRING, Dep_from_Normal STRING, Avg_Dew_Pt STRING, Avg_Wet_Bulb STRING, Heating_Degree_Days STRING,
Cooling_Degree_Days STRING, Significant_Weather STRING, Snow_Ice_Depth STRING, Snow_Ice_Water_Equiv STRING,
Precipitation_Snowfall STRING, Precipitation_Water_Equiv STRING, Pressue_Avg_Station STRING,
Pressure_Avg_Sea_Level STRING, Wind_Speed STRING, Wind_Direction STRING, Wind_Avg_Speed STRING, Max_5_sec_speed STRING,
Max_5_sec_Dir STRING, Max_2_min_speed STRING, Max_2_min_Dir STRING)
PARTITIONED BY (INGESTION_DT STRING) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';

-- fill table with data from s3
ALTER TABLE 165430_ing_m_lab3 ADD PARTITION (INGESTION_DT ='2019-01-01') LOCATION '/data/2019-01-01';
ALTER TABLE 165430_ing_m_lab3 ADD PARTITION (INGESTION_DT ='2019-01-02') LOCATION '/data/2019-01-02';
ALTER TABLE 165430_ing_m_lab3 ADD PARTITION (INGESTION_DT ='2019-01-03') LOCATION '/data/2019-01-03';
ALTER TABLE 165430_ing_m_lab3 ADD PARTITION (INGESTION_DT ='2019-01-04') LOCATION '/data/2019-01-04';
ALTER TABLE 165430_ing_m_lab3 ADD PARTITION (INGESTION_DT ='2019-01-05') LOCATION '/data/2019-01-05';
ALTER TABLE 165430_ing_m_lab3 ADD PARTITION (INGESTION_DT ='2019-01-06') LOCATION '/data/2019-01-06';
ALTER TABLE 165430_ing_m_lab3 ADD PARTITION (INGESTION_DT ='2019-01-07') LOCATION '/data/2019-01-07';
ALTER TABLE 165430_ing_m_lab3 ADD PARTITION (INGESTION_DT ='2019-01-08') LOCATION '/data/2019-01-08';
ALTER TABLE 165430_ing_m_lab3 ADD PARTITION (INGESTION_DT ='2019-01-09') LOCATION '/data/2019-01-09';
ALTER TABLE 165430_ing_m_lab3 ADD PARTITION (INGESTION_DT ='2019-01-10') LOCATION '/data/2019-01-10';

-- show all partitions in created table
show partitions 165430_ing_m_lab3;

-- count elements in table
Select count(*) from 165430_ing_m_lab3;

-- count average MaxTemp in data
select avg(MaxTemp) from 165430_ing_m_lab3;
select avg(cast(MaxTemp as float)) from 165430_ing_m_lab3;

-- count max Wind Speed in data
select max(cast(Wind_Speed as float)) from 165430_ing_m_lab3;
select max(distinct(cast(Wind_Speed as float))) from 165430_ing_m_lab3;

-- count min Wind Speed in data
select min(cast(Wind_Speed as float)) from 165430_ing_m_lab3;
select min(distinct(cast(Wind_Speed as float))) from 165430_ing_m_lab3;

-- find 5 unique max values of Pressure_Avg_Sea_Level in data
select distinct Pressure_Avg_Sea_Level from 165430_ing_m_lab3 order by Pressure_Avg_Sea_Level desc LIMIT 5;

-- find 5 unique min values of Pressure_Avg_Sea_Level in data
select distinct Pressure_Avg_Sea_Level from 165430_ing_m_lab3 order by Pressure_Avg_Sea_Level asc LIMIT 5;

-- print value of Wind Speed and it value is between 0 and 5 print "SLABY" or if value is between 6 and 12 print
-- "SREDNI" or if value is between 12 and 35 print "MOCNY"
select Wind_Speed, if(cast(Wind_Speed as float) > 0 and cast(Wind_Speed as float) <= 5, "SLABY", "") from 165430_ing_m_lab3;
select Wind_Speed, if(cast(Wind_Speed as float) > 6 and cast(Wind_Speed as float) <= 12, "SREDNI", "") from 165430_ing_m_lab3;
select Wind_Speed, if(cast(Wind_Speed as float) > 12 and cast(Wind_Speed as float) < 35, "MOCNY", "") from 165430_ing_m_lab3;

