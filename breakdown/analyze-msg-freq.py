from datetime import date
import argparse
import numpy as np
import matplotlib.pyplot as plt

# Arguements
parser = argparse.ArgumentParser(description='Generate a graph based on message frequency and times throughout the days')
parser.add_argument('csv', metavar='csv', type=str, help='csv file location')
args = parser.parse_args()

# Days to accumulate message frequency
class Days:
    days = {}

    def analyse_days(self, s):
        try:
            self.days[s] = self.days[s] + 1
        except:
            self.days[s] = 1

    def self_print(self):
        for i in self.days:
            print(i, self.days[i])

# Useful functions to convert fb-msg data into datetime
# Converts month to numbers
def month_converter(month):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    return months.index(month) + 1

# Returns date object from date str
# provided from fb
def date_analyze(s):
    s = s.split(' ')
    day_num = s[1]
    month_num = month_converter(s[0])
    year_num = s[2]

    return date(int(year_num), int(month_num), int(day_num))

# Variables
days = Days()

# Opens csv file (comma separated values: csv)
#

# Read first line in order to get first date
with open(args.csv, 'rv') as f:
    found_first = False
    for line in f.readlines():
        if not found_first:
            try:
                csv_first = line.split(',')
                date_first = date_analyze(csv_first[2])
                found_first = True 
            except:
                pass
        else:
            pass
    # Read last line in order to get last date
    csv_last = line.split(',')
    date_last = date_analyze(csv_last[2])

# Compute difference of days
# Analyze data accordingly to prepare data
delta_days = (date_first - date_last).days
print(delta_days)

# Use previous findings to organize data
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

days.self_print()

x = [i for i in range(0, len(days.days))]
y = [days.days[i] for i in days.days] 

print(x)
print(y)

