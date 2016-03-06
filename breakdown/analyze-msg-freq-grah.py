from datetime import date
from matplotlib.font_manager import FontProperties
import argparse
import numpy as np
import matplotlib.pyplot as plt

# Color palette
blue = '#3498db' 
red = '#e74c3c'
green = '#2ecc71'


# Our font
font_default = FontProperties()
font_default.set_family('sans-serif')
font_default.set_weight('bold')

# Arguements
parser = argparse.ArgumentParser(description='Generate a graph based on message frequency and times throughout the days')
parser.add_argument('csv', metavar='csv', type=str, help='csv file location')
parser.add_argument('-sd', dest='sd', const='2015-01-01', action='store', nargs='?', type=str, help='only start displaying from date') 
parser.add_argument('-ed', dest='ed', const='2016-01-01', action='store', nargs='?', type=str, help='don\'t display after this date') 
args = parser.parse_args()

# Useful functions to convert fb-msg data into datetime
# Converts numbers to month
def num_to_month(num):
    nums = {'1': 'Jan', '2': 'Feb', '3': 'Mar', '4': 'Apr', '5': 'May', '6': 'Jun', '7': 'Jul', '8': 'Aug', '9': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
    return nums[num]

# Returns date object from date str
# provided from fb
# ACCEPTS A STRING FROM FB-FORMATTED DATETIME (separated with spaces)
def date_analyze(s):
    s = s.split('-')
    day_num = s[2]
    month_num = s[1]
    year_num = s[0]

    return date(int(year_num), int(month_num), int(day_num))

# Creates a label for the x axis
#!!! ACCEPTS A DATE OBJECT (import from datetime) !!
#
def date_labels(rdate):
    month = num_to_month(str(rdate.month))
    return str(rdate.day) + ' ' + month + ' ' + str(rdate.year)

# Opens csv file (comma separated values: csv)
#
#
# Read first line in order to get LAST date
# ORGANIZED FROM MOST RECENT TO OLDEST
with open(args.csv, 'rv') as f:
    found_last = False
    for line in f.readlines():
        if not found_last:
            try:
                csv_last = line.split(',')
                date_last = date_analyze(csv_last[2])
                found_last = True 
            except:
                pass
        else:
            pass
    # Read last line in order to get last date
    csv_first = line.split(',')
    date_first = date_analyze(csv_first[2])

# Compute difference of days
# Analyze data accordingly to prepare data
#

date_first = date(date_first.year, date_first.month, 1) # First day of oldest message (makes data look neater)

# If user has defined his own start date
if args.sd:
    buffer_list = args.sd.split('-')
    date_first = date(int(buffer_list[0]), int(buffer_list[1]), int(buffer_list[2]))
    

# If user has defined his own end date
if args.ed:
    buffer_list = args.ed.split('-')
    date_last = date(int(buffer_list[0]), int(buffer_list[1]), int(buffer_list[2]))

delta_days = (date_last - date_first).days # Difference in days (to index things)

# Data points
x_data = np.arange(delta_days) # our x-axis data
y_data = [0 for i in range(0, delta_days)] # our y-axis data
x_labels = [] # labels for the x axis
x_labels_tick = [] # where the labels appear on the x-axis

# Read csv files and process
with open(args.csv, 'rv') as f:
    for line in f.readlines():
        try:
            csv_vals = line.split(',')

            # Get date
            cur_date = date_analyze(csv_vals[2])

            # if its within the dates
            if cur_date >= date_first and cur_date <= date_last:
                delta_days_index = (date_last-cur_date).days

                # Increment message count via indexing
                y_data[delta_days_index] = y_data[delta_days_index] + 1

        except:
            pass

# Organize labels according to month
buffer_date = date_first
while buffer_date <= date_last:
    x_labels.append(date_labels(buffer_date))
    x_labels_tick.append((buffer_date-date_first).days)

    try:
        buffer_date = date(buffer_date.year, buffer_date.month + 1, buffer_date.day)
    except:
        buffer_date = date(buffer_date.year + 1, 1, buffer_date.day)

# First date label
if date_labels(date_first) not in x_labels:
    x_labels.insert(0, date_labels(date_first))
    x_labels_tick.insert(0, (date_first-date_first).days)

# Last date label
if date_labels(date_last) not in x_labels:
    x_labels.append(date_labels(date_last))
    x_labels_tick.append((delta_days-1))

# Reverse our data point
# as fb's data starts from latest to oldest
y_data = y_data[::-1]

# Create graph
fig, ax = plt.subplots(facecolor='white')

# Plot data
plt.plot(x_data, y_data, color=blue, linewidth=2.5)
plt.text(delta_days, y_data[-1], 'Total messages', fontproperties=font_default, fontsize=12, color=blue)

# Set graph limit 
ax.set(xlim=(0, len(x_data)-1), ylim=(0, None))

# Add tick lines across y-axis to trace data more easily
y_axis_labels = ax.get_yticks()
buffer_i = int(y_axis_labels[1]) # Gets the first tick range for the y-axis
buffer_i_max = int(y_axis_labels[-1])
for buffer_y in range(0, buffer_i_max+1, buffer_i):
    plt.plot(range(0, delta_days), [buffer_y]*len(range(0, delta_days)), '--', lw=0.5, color='black', alpha=0.3)
plt.axhline(0, color='black', alpha=0.3)

# Remove the tick marks; they are unnecessary with the tick lines we just plotted.
plt.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off", labelleft="on")

# Set background color
ax.set_axis_bgcolor('white')

# Remove plot frame lines
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

# Remove unncessary chartjunk
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()

# Set axis label
#plt.ylabel('messages per day')
#plt.xlabel('date')

# Set labels position and text
ax.set_xticks(x_labels_tick )
ax.set_xticklabels(x_labels)

# Sets window title
fig.canvas.set_window_title('Number of messages sent daily')

# Make sure labels are have enough room
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.setp(ax.get_xticklabels(), rotation=35)

# Shows graph
plt.show()

