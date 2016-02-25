import matplotlib.pyplot as plt
import argparse

# Arguements
parser = argparse.ArgumentParser(description='Generate wordcloud images from csv-formatted fb convo data')
parser.add_argument('-y', dest='year', const=2015, action='store', nargs='?', type=int, help='only display wordclouds from this year') # If year is not specify then wordcloud will be generated from everything
parser.add_argument('-ob', help='output both user\'s combined wordcloud', action='store_true') # Combine both users messages into a wordcloud too
parser.add_argument('csv', metavar='csv', type=str, help='csv file location')
parser.add_argument('ol', metavar='ol', type=str, help='output FOLDER location')
args = parser.parse_args()

# Opens csv file (comma separated values: csv)
with open(args.csv, 'rb') as f:
    for line in f.readlines():
        print line.split(',')
