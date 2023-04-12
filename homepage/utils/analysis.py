from pyspark.sql import SparkSession
from pyspark.sql.functions import col, regexp_replace
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import holoviews as hv
from holoviews import opts
hv.extension('bokeh')
# from holoviews.plotting.bokeh import HoverTool


def chart0(df):
    plt.plot(df.index, df['temperature'])
    plt.xlabel('mycolumn')
    plt.ylabel('myvalue')

    plt.savefig('/Users/phanngl/Documents/bigdata/project/toshakana/homepage/static/img/chart/plot.png')

def chart1(df):

    chart = hv.Distribution(df['temperature']).opts(title="Temperature Distribution", color="green", xlabel="Temperature", ylabel="Density")\
                            .opts(opts.Distribution(width=700, height=300,tools=['hover'],show_grid=True))
    
    # chart = hv.Distribution(df['temperature']).opts(
    #     title="Temperature Distribution",
    #     color="green",
    #     xlabel="Temperature",
    #     ylabel="Density"
    # ).opts(
    # opts.Distribution(width=700, height=300, hooks=[HoverTool()])
    # )

    hv.save(chart, '/Users/phanngl/Documents/bigdata/project/toshakana/homepage/static/img/chart/chart1.png', fmt='png')

    # plt.hist(df['temperature'], bins=300, color='green')
    # plt.xlabel('Temperature')
    # plt.ylabel('Density')
    # plt.title('Temperature Distribution')
    # plt.savefig('/Users/phanngl/Documents/bigdata/project/toshakana/homepage/static/img/chart/chart1.png')