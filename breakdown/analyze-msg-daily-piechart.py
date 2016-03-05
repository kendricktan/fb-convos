from datetime import date
import argparse
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

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

x = [i for i in range(0, len(days.days))]
y = [days.days[i] for i in days.days] 

