from django.shortcuts import render
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
# from io import BytesIO
# import base64
from pyspark.sql import SparkSession
from homepage.utils.analysis import *



def homepage(request):

    # spark = SparkSession.builder\
    #         .appName("pandas-streaming")\
    #         .config("spark.driver.extraClassPath", "/usr/local/Cellar/apache-spark/3.3.2/libexec/jars/mysql-connector-java-8.0.13.jar") \
    #         .config("spark.executor.extraClassPath", "/usr/local/Cellar/apache-spark/3.3.2/libexec/jars/mysql-connector-java-8.0.13.jar") \
    #         .config("spark.ui.port", "4041")\
    #         .getOrCreate()
    
        
    # url = "jdbc:mysql://localhost:3306/weather_his"
    # table1 = "weather"
    # table2 = "df"
    # table3 = "resampled_df"
    # table4 = "resampled_days"
    # properties = {"user": "root", "password": "12345678"}



    
    # df1 = spark.read.jdbc(url=url, table= table1, properties=properties)
    # test_df = df1.toPandas()
    # result = test_df[['id', 'temperature']].head(100)
    # result = test1_df.groupby('precip_type').sum()
    # chart0(result)


    # df = spark.read.jdbc(url=url, table= table2, properties=properties)
    # df = df.toPandas()
    # chart1(df)



    return render(request, 'index.html', {})

# pyspark --driver-class-path /usr/local/Cellar/apache-spark/3.3.2/libexec/jars/mysql-connector-java-8.0.13.jar --jars /usr/local/Cellar/apache-spark/3.3.2/libexec/jars/mysql-connector-java-8.0.13.jar
#     /usr/local/Cellar/apache-spark/3.3.2/libexec/jars/mysql-connector-java-8.0.13.jar 
