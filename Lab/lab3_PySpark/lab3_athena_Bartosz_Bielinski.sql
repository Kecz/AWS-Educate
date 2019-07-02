-- in Athena:
/* After saving data in bucket with PySpark:
From S3 bucket:
"s3://bartosz-bielinski/lab3-data/"
create DataBase named "lab3" with table "meteodata" with columns of types:

Wban_Number STRING, YearMonthDay STRING, Max_Temp STRING, Min_Temp STRING, Avg_Temp STRING, Dep_from_Normal STRING,
Avg_Dew_Pt STRING, Avg_Wet_Bulb STRING, Heating_Degree_Days STRING, Cooling_Degree_Days STRING,
Significant_Weather STRING, Snow_Ice_Depth STRING, Snow_Ice_Water_Equiv STRING, Precipitation_Snowfall STRING,
Precipitation_Water_Equiv STRING, Pressue_Avg_Station STRING, Pressure_Avg_Sea_Level STRING, Wind_Speed STRING,
Wind_Direction STRING, Wind_Avg_Speed STRING, Max_5_sec_speed STRING, Max_5_sec_Dir STRING, Max_2_min_speed STRING,
Max_2_min_Dir STRING

From S3 bucket: "s3://bartosz-bielinski/lab3-data/"
*/
-- You can check data in table with:
select * from "lab3"."meteodata" limit 10;

-- Finding average value from all maximum temperatures
select avg(try_cast(Max_Temp as double)) from "lab3"."meteodata"

-- Find max value in Wind Speed
select max(try_cast(Wind_Speed as double)) from "lab3"."meteodata"

-- Find min value in Wind Speed
select min(try_cast(Max_Temp as double)) from "lab3"."meteodata"

-- Find 5 unique max values of Pressure_Avg_Sea_Level in data
select distinct Pressure_Avg_Sea_Level from "lab3"."meteodata" order by Pressure_Avg_Sea_Level desc LIMIT 5;

-- Find 5 unique min values of Pressure_Avg_Sea_Level in data
select distinct Pressure_Avg_Sea_Level from "lab3"."meteodata" order by Pressure_Avg_Sea_Level asc LIMIT 5;
