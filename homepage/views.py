from django.shortcuts import render
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from pyspark.sql import SparkSession


def homepage(request):

    spark = SparkSession.builder\
            .appName("pandas-streaming")\
            .config("spark.driver.extraClassPath", "/usr/local/Cellar/apache-spark/3.3.2/libexec/jars/mysql-connector-java-8.0.13.jar") \
            .config("spark.executor.extraClassPath", "/usr/local/Cellar/apache-spark/3.3.2/libexec/jars/mysql-connector-java-8.0.13.jar") \
            .config("spark.ui.port", "4041")\
            .getOrCreate()
    
    #spark = SparkSession.builder.appName("pandas-streaming").config("spark.driver.extraClassPath", "/usr/local/Cellar/apache-spark/3.3.2/libexec/jars/mysql-connector-java-8.0.13.jar").config("spark.executor.extraClassPath", "/usr/local/Cellar/apache-spark/3.3.2/libexec/jars/mysql-connector-java-8.0.13.jar").getOrCreate()
    # df = spark.read.format("jdbc").option("url", "jdbc:mysql://localhost/weather_his").option("dbtable", "weather").option("user", "root").option("password", "12345678").load() 
    
    
    url = "jdbc:mysql://localhost:3306/weather_his"
    table = "weather"
    properties = {"user": "root", "password": "12345678"}
    df = spark.read.jdbc(url=url, table= table, properties=properties)
    test_df = df.toPandas()
    result = test_df[['id', 'temperature']].head(100)
    # result = test1_df.groupby('precip_type').sum()

   # df = spark.read.jdbc(url="jdbc:mysql://localhost:3306/weather_his", table= "weather", properties={"user": "root", "password": "12345678"})

    plt.plot(result.index, result['temperature'])
    plt.xlabel('mycolumn')
    plt.ylabel('myvalue')

    # plt.savefig('static/img/plot.png')

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    img_data = base64.b64encode(buffer.getvalue()).decode()
    img_tag = f'<img src="data:image/png;base64,{img_data}"/>'

    with open('/Users/phanngl/Documents/bigdata/project/toshakana/homepage/templates/index.html', 'r') as f:
        html = f.read()

    html = html.replace('<div id="mydiv"></div>', f'<div id="mydiv">{img_tag}</div>')

    with open('/Users/phanngl/Documents/bigdata/project/toshakana/homepage/templates/index.html', 'w') as f:
        f.write(html)


    return render(request, 'index.html', {})

# pyspark --driver-class-path /usr/local/Cellar/apache-spark/3.3.2/libexec/jars/mysql-connector-java-8.0.13.jar --jars /usr/local/Cellar/apache-spark/3.3.2/libexec/jars/mysql-connector-java-8.0.13.jar
#     /usr/local/Cellar/apache-spark/3.3.2/libexec/jars/mysql-connector-java-8.0.13.jar 
