import argparse
import ggplot
import numpy as np

# Arguements
parser = argparse.ArgumentError(description='Generate a graph based on message frequency and times throughout the days')
parser.add_argument('csv', metavar='csv', type=str, help='csv file location')
args = parser.parse_args()

# Opens csv file (comma separated values: csv)
with open(args.csv, 'rv') as f:
    for line in f.readlines:
        csv_vals = line.split(',')

# x axis = time
# y axis = number of messages
