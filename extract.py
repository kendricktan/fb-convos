import os
import sys
import argparse

# Python version warning
if sys.version_info.major < 3:
    print("** WARNING: This script was built for python 3, using python 2 might cause some unexpected issues **")

# Command line arguements
parser = argparse.ArgumentParser(description='Extract and format fb messages to be analyzed')
parser.add_argument('infile', metavar='if', type=str, help='in-file location')
parser.add_argument('outfile', metavar='of', type=str, help='out-file location')
parser.add_argument('user1', metavar='u1', type=str, help='User 1\'s name within the conversation')
parser.add_argument('user2', metavar='u2', type=str, help='User 2\'s name within the conversation')
args = parser.parse_args()
#print(args.infile)

raw_msg_file = open(args.infile, 'r')
fmt_msg_file = open(args.outfile, 'w')

