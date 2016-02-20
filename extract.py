import os
import sys
import argparse
import re

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

# Read files
raw_msg_file = open(args.infile, 'r')
fmt_msg_file = open(args.outfile, 'w')

# Get user names
user1_name = args.user1
user2_name = args.user2

regex_exp = r'<div class="message"><div class="message_header"><span class="user">\w*\s*' + user1_name + '\s*\w*</span><span class="meta">(.*?)</span></div></div><p>(.*?)</p>'

for raw_line in raw_msg_file:
    matches = re.findall(regex_exp, raw_line)

    for match in matches:
        print(match)
