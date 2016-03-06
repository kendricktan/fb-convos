from datetime import date
import operator
import argparse
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Arguements
parser = argparse.ArgumentParser(description='Generate a pie chart to show the distribution of messages according to day')
parser.add_argument('csv', metavar='csv', type=str, help='csv file location')
args = parser.parse_args()

# Days to accumulate message frequency
class Days:
    days = {'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0, 'Sunday': 0}
    days_sorted = []

    # Analyze raw days from fb messages
    def analyse_days(self, s):
        try:
            self.days[s] = self.days[s] + 1
        except:
            self.days[s] = 1


    # Sort dict according to freq
    def sort_days(self):
        self.days_sorted = sorted(self.days.items(), key=operator.itemgetter(1), reverse=True)

    # Debug print
    def self_print(self):
        for i in self.days:
            print(i, self.days[i])
        print(self.days_sorted)

# Variables
days = Days()

# Pie chart display for average messages per day
#
with open(args.csv, 'rv') as f:
    for line in f.readlines():
        try:
            csv_vals = line.split(',')
            #
            # csv_vals[0] = Sender name
            # csv_vals[1] = Day
            # csv_vals[2] = Date
            # csv_vals[3] = Time
            #
            days.analyse_days(csv_vals[1])
        except:
            pass

# Sort days
days.sort_days()

colors = sns.color_palette('coolwarm', 7) # Colors used for pie chart
explode = [0.2, 0, 0, 0, 0, 0, 0] # Only explode the largest piece
chart_data_dist = [] # Distribution of data
chart_labels = [] # Labels for distribution of data

for days_buffer in days.days_sorted:
    chart_labels.append(days_buffer[0])
    chart_data_dist.append(days_buffer[1])

#print('data_dist', chart_data_dist)
#print('data_labels', chart_labels)

# Creates our figure
fig = plt.figure(figsize=[10, 10])
ax = fig.add_subplot(111)

# Styles the pie chart
pie_wedge_collection = ax.pie(chart_data_dist, labels=chart_labels, autopct='%1.1f%%', startangle=90, colors=colors, explode=explode)

for pie_wedge in pie_wedge_collection[0]:
    pie_wedge.set_edgecolor('white')

fig.canvas.set_window_title('Chat distribution')
plt.axis('equal') # make piechart circular
plt.show()
