import argparse
import numpy as np
import matplotlib.pyplot as plt

# To do:
# Add argument for displaying graph in hours; or days; or months;

# Arguements
parser = argparse.ArgumentParser(description='Generate a graph based on message frequency and times throughout the days')
parser.add_argument('csv', metavar='csv', type=str, help='csv file location')
args = parser.parse_args()

# Variables

# Days to accumulate message frequency
class Days:
    Monday = 0 
    Tuesday = 0
    Wednesday = 0
    Thursday = 0
    Friday = 0
    Saturday = 0
    Sunday = 0

    def analyse_days(self, s):
        if 'monday' in s.lower():
            self.Monday = self.Monday + 1
        elif 'tuesday' in s.lower():
            self.Tuesday = self.Tuesday + 1
        elif 'wednesday' in s.lower():
            self.Wednesday = self.Wednesday + 1
        elif 'thursday' in s.lower():
            self.Thursday = self.Thursday + 1
        elif 'friday' in s.lower():
            self.Friday = self.Friday + 1
        elif 'saturday' in s.lower():
            self.Saturday = self.Saturday + 1
        elif 'sunday' in s.lower():
            self.Sunday = self.Sunday + 1

    def self_print(self):
        print('Monday: ' + str(self.Monday))
        print('Tuesday: ' + str(self.Tuesday)) 
        print('Wednesday: ' + str(self.Wednesday)) 
        print('Thursday: ' + str(self.Thursday)) 
        print('Friday: ' + str(self.Friday)) 
        print('Saturday: ' + str(self.Saturday)) 
        print('Sunday: ' + str(self.Sunday)) 

days = Days()

# Opens csv file (comma separated values: csv)
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

#x_data = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
x_data = (1,2,3,4,5,6,7)
y_data = (days.Monday, days.Tuesday, days.Wednesday, days.Thursday, days.Friday, days.Saturday, days.Sunday)

fig = plt.figure()
plt.bar(x_data, y_data, width=100)

#days.self_print()

# x axis = time
# y axis = number of messages
