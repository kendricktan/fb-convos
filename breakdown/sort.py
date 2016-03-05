from datetime import date, datetime
import argparse
import numpy as np
import matplotlib.pyplot as plt
import csv

# Arguements
parser = argparse.ArgumentParser(description='Generate a graph based on message frequency and times throughout the days')
parser.add_argument('csv', metavar='csv', type=str, help='csv file location')
args = parser.parse_args()

csv_file = csv.reader(open(args.csv,'r'))
sortedlist = sorted(csv_file, key=operator.itemgetter(2), reverse=True)

