from django.shortcuts import render
import matplotlib
matplotlib.use('Agg')
from pyspark.sql import SparkSession


# from homepage.utils.analysis import *

# from background_task.models import Task
# task_obj = Task.objects.create(
#     task_name='homepage', 
#     task_func='homepage',
#     schedule_type=Task.SCHEDULE_INTERVAL,
#     schedule='60', # Run every 60 seconds
#     repeat=None
# )



# @background(schedule=60)
def homepage(request):

    spark = SparkSession.builder\
            .appName("pandas-streaming")\
            .config("spark.driver.extraClassPath", "/usr/local/Cellar/apache-spark/3.3.2/libexec/jars/mysql-connector-java-8.0.13.jar") \
            .config("spark.executor.extraClassPath", "/usr/local/Cellar/apache-spark/3.3.2/libexec/jars/mysql-connector-java-8.0.13.jar") \
            .config("spark.ui.port", "4041")\
            .getOrCreate()
    
        
    url = "jdbc:mysql://localhost:3306/weather_his"
    table1 = "weather"
    table2 = "df"
    table3 = "resampled_df"
    table4 = "resampled_days"
    properties = {"user": "root", "password": "12345678"}

    
    # df1 = spark.read.jdbc(url=url, table= table1, properties=properties)
    # test_df = df1.toPandas()
    # result = test_df[['id', 'temperature']].head(100)
    # result = test1_df.groupby('precip_type').sum()
    # chart0(result)


    df = spark.read.jdbc(url=url, table= table2, properties=properties)
    df = df.toPandas()
    chart1(df)
    chart2(df)
    chart3(df)
    chart4(df)
    chart5(df)
    chart9(df)


    resampled_df = spark.read.jdbc(url=url, table= table3, properties=properties)
    resampled_df = resampled_df.toPandas()
    chart6(resampled_df) 
    chart7(resampled_df)  
    chart10(resampled_df) 
    chart11(resampled_df) 
    chart13(resampled_df) 
    chart16(resampled_df) 

    resampled_days = spark.read.jdbc(url=url, table= table4, properties=properties)
    resampled_days = resampled_days.toPandas()
    chart14(resampled_days) 

    return render(request, 'index.html', {})

# pyspark --driver-class-path /usr/local/Cellar/apache-spark/3.3.2/libexec/jars/mysql-connector-java-8.0.13.jar --jars /usr/local/Cellar/apache-spark/3.3.2/libexec/jars/mysql-connector-java-8.0.13.jar
#     /usr/local/Cellar/apache-spark/3.3.2/libexec/jars/mysql-connector-java-8.0.13.jar 
