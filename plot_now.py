# bokeh is used to plot and run the graph in the browser in real time
from bokeh.models import ColumnDataSource, DatetimeTickFormatter, NumeralTickFormatter
from bokeh.plotting import curdoc, figure
import pandas as pd  # to put the data in dataframe data structure to simplify interaction with it
import requests  # to make requests to the Deribit API and get necessary data


df = pd.DataFrame(columns=['time', 'funding_rate', 'rolling_rate'])  # create empty dataframe
# TODO add past data
source = ColumnDataSource(df)  # to map column names and lists of data (to plot data)


def update():
    """ get json object from the exchange and access timestamp and 8h funding rate from it
     attach this to dataframe and plot the last row"""
    raw = requests.get('https://test.deribit.com/api/v2/public/ticker?instrument_name=BTC-PERPETUAL')
    raw_json = raw.json()
    time_stamp = int(raw_json['result']['timestamp'])
    rate = raw_json['result']['current_funding']

    global df  # access df from outer scope
    df = df.append({'time': time_stamp, 'funding_rate': rate}, ignore_index=True)

    # rolling rate based on 4h hours (14400 seconds)
    df['rolling_rate'] = df['funding_rate'].rolling(14400, min_periods=0).mean()
    source.stream(df.iloc[[-1]], rollover=15000)  # stream last row, rollover is used to store less than 15k values


# create the figure on which data is plotted
p = figure(width=1000, plot_height=500,
           title='Deribit Real Time 8h Funding Rate vs 4h Rolling Rate',
           y_axis_location='right',
           x_axis_type='datetime',
           x_axis_label='Time',
           y_axis_label='Funding Rate',
           toolbar_location="below"
           )

p.x_range.follow="end"  # plot the point at the end of the graph
p.x_range.follow_interval=70000  # 100k == 15sec distance between ticks
p.x_range.range_padding=0

# format x and y axis to Hours/Minutes/Seconds on x and 6 decimal points on y
p.xaxis.formatter = DatetimeTickFormatter(minutes="%H:%M:%S")
p.yaxis.formatter=NumeralTickFormatter(format="0.000000")

# add lines and data points on them
p.line(x='time', y='funding_rate', source=source, color='blue', legend="8h Funding Rate", line_width=2, alpha=0.5)
p.circle(x='time', y='funding_rate', source=source, color="blue", size=3)
p.line(x='time', y='rolling_rate', source=source, color="black", legend="4h Rolling Rate", line_width=1, alpha=0.7)
p.circle(x='time', y='rolling_rate', source=source, color="black", size=3)

p.line(x='time', y=0, source=source, line_width=1, alpha=0.4, color='blue')  # 0 level

p.xaxis.major_label_orientation = 3.0/4.0
# p.yaxis[0].ticker.desired_num_ticks = 10

p.toolbar.autohide = True
p.legend.location = "bottom_left"

# TODO display current values outside of the plot for clarity
doc = curdoc()
doc.add_root(p)
doc.add_periodic_callback(update, 1000)  # call the function every second (100 = every 0.1s, 10,000 = 10s)

# to start the app
# bokeh serve --show plot_now.py

# TODO put app on the server
