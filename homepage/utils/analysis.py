from pyspark.sql import SparkSession
from pyspark.sql.functions import col, regexp_replace
import matplotlib
matplotlib.use('Agg')
import holoviews as hv
from holoviews import opts
hv.extension('bokeh')
import pandas as pd

import matplotlib.pyplot    as plt
import plotly.express       as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
# from holoviews.plotting.bokeh import HoverTool
import numpy  as np


def chart0(df):
    plt.plot(df.index, df['temperature'])
    plt.xlabel('mycolumn')
    plt.ylabel('myvalue')

    plt.savefig('/Users/phanngl/Documents/bigdata/project/toshakana/homepage/static/img/chart/plot.png')

def chart1(df):

    chart = hv.Distribution(df['temperature']).opts(title="Temperature Distribution", color="green", xlabel="Temperature", ylabel="Density")\
                            .opts(opts.Distribution(width=700, height=300,tools=['hover'],show_grid=True))
    hv.save(chart, '/Users/phanngl/Documents/bigdata/project/toshakana/homepage/static/img/chart/chart1.png', fmt='png')


def chart2(df):
    season_cnt = np.round(df['season'].value_counts(normalize=True) * 100)
    chart = hv.Bars(season_cnt).opts(title="Season Count", color="red", xlabel="Season", ylabel="Percentage", yformatter='%d%%')\
            .opts(opts.Bars(width=700, height=300,tools=['hover'],show_grid=True))

    hv.save(chart, '/Users/phanngl/Documents/bigdata/project/toshakana/homepage/static/img/chart/chart2.png', fmt='png')

def chart3(df):
    timing_cnt = np.round(df['timing'].value_counts(normalize=True) * 100)
    chart = hv.Bars(timing_cnt).opts(title="Timing Count", color="black", xlabel="Timing", ylabel="Percentage", yformatter='%d%%')\
            .opts(opts.Bars(width=700, height=300,tools=['hover'],show_grid=True))

    hv.save(chart, '/Users/phanngl/Documents/bigdata/project/toshakana/homepage/static/img/chart/chart3.png', fmt='png')

def chart4(df):
    season_agg = df.groupby('season').agg({'temperature': ['min', 'max']})
    season_maxmin = pd.merge(season_agg['temperature']['max'],season_agg['temperature']['min'],right_index=True,left_index=True)
    season_maxmin = pd.melt(season_maxmin.reset_index(), ['season']).rename(columns={'season':'Season', 'variable':'Max/Min'})
    chart = hv.Bars(season_maxmin, ['Season', 'Max/Min'], 'value').opts(title="Temperature by Season Max/Min", ylabel="Temperature")\
                                                                .opts(opts.Bars(width=700, height=300,tools=['hover'],show_grid=True))

    hv.save(chart, '/Users/phanngl/Documents/bigdata/project/toshakana/homepage/static/img/chart/chart4.png', fmt='png')

def chart5(df):
    timing_agg = df.groupby('timing').agg({'temperature': ['min', 'max']})
    timing_maxmin = pd.merge(timing_agg['temperature']['max'],timing_agg['temperature']['min'],right_index=True,left_index=True)
    timing_maxmin = pd.melt(timing_maxmin.reset_index(), ['timing']).rename(columns={'timing':'Timing', 'variable':'Max/Min'})
    chart = hv.Bars(timing_maxmin, ['Timing', 'Max/Min'], 'value').opts(title="Temperature by Timing Max/Min", ylabel="Temperature")\
                                                                .opts(opts.Bars(width=700, height=300,tools=['hover'],show_grid=True))

    hv.save(chart, '/Users/phanngl/Documents/bigdata/project/toshakana/homepage/static/img/chart/chart5.png', fmt='png')

def chart6(resampled_df):
    fig = px.line(resampled_df,x=resampled_df.index,y=['temperature','humidity','wind_speed','visibility','loud_cover','pressure'],title='All features distribution')
    # ############

    fig.write_image('/Users/phanngl/Documents/bigdata/project/toshakana/homepage/static/img/chart/chart6.png', format='png')


def chart7(resampled_df):
    fig = px.line(resampled_df,x=resampled_df.index,y=['temperature','humidity','wind_speed','visibility','loud_cover'],title='All features distribution withot Pressure (millibars)')
    #################
    fig.write_image('/Users/phanngl/Documents/bigdata/project/toshakana/homepage/static/img/chart/chart7.png', format='png')

def chart9(df):
    in_month = df[df['formatted_is_month_start']=='Yes'].groupby('formatted_month').agg({'humidity':['mean']})
    in_month.columns = [f"{i[0]}_{i[1]}" for i in in_month.columns]
    out_month = df[df['formatted_is_month_start']=='No'].groupby('formatted_month').agg({'humidity':['mean']})
    out_month.columns = [f"{i[0]}_{i[1]}" for i in out_month.columns]
    chart = hv.Curve(in_month, label='Yes') * hv.Curve(out_month, label='No').opts(
        title="Average Humidity by month start", ylabel="Humidity", xlabel='Month')\
        .opts(opts.Curve(width=700, height=300,tools=['hover'],show_grid=True))

    hv.save(chart, '/Users/phanngl/Documents/bigdata/project/toshakana/homepage/static/img/chart/chart9.png', fmt='png')

def chart10(resampled_df):
    fig = px.line(resampled_df, x=resampled_df.index, y="temperature", title = "Average Monthly Temperature (C)")


    fig.write_image('/Users/phanngl/Documents/bigdata/project/toshakana/homepage/static/img/chart/chart10.png', format='png')

def chart11(resampled_df):
    fig = px.bar(resampled_df, x=resampled_df.index, y="temperature", title = "Average Monthly Temperature (C)")


    fig.write_image('/Users/phanngl/Documents/bigdata/project/toshakana/homepage/static/img/chart/chart11.png', format='png')


def chart13(resampled_df):
    fig = px.line(resampled_df, x=resampled_df.index, y='humidity',  title = "Average Monthly Humidity")


    fig.write_image('/Users/phanngl/Documents/bigdata/project/toshakana/homepage/static/img/chart/chart13.png', format='png')

def chart14(resampled_days):
    dayly_df = resampled_days
    fig = px.line(dayly_df, x = dayly_df.index, y = "pressure",title = "Average Dayly Pressure (millibars) over the year")


    fig.write_image('/Users/phanngl/Documents/bigdata/project/toshakana/homepage/static/img/chart/chart13.png', format='png')


def chart16(resampled_df):
    fig = px.line(resampled_df, x=resampled_df.index, y='humidity', title='Time Series with Range Slider and Selectors')

    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        )
    )

    fig.write_image('/Users/phanngl/Documents/bigdata/project/toshakana/homepage/static/img/chart/chart13.png', format='png')

