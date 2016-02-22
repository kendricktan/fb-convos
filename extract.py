import argparse
import re

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

# Regular expression
regex_exp = r'<div class="message"><div class="message_header"><span class="user">(.*?)</span><span class="meta">(.*?)</span></div></div><p>(.*?)</p>'

# Our final string to be written onto the file
string_final = ''

################################ RULES #####################################
#
# > Conversation will be considered initiated if there isn't any previous 
# conversation between the two for 15 minutes
#
# > Since facebook organizes the message really untidily, it'll only extract
# messages which you (user 1) initiate, and which user 2 ends with or 
# continue, or vice-versa
#
############################################################################

for raw_line in raw_msg_file:
    # Find regular expression
    matches = re.findall(regex_exp, raw_line)

    # String buffer to be concatentated
    # into the final string
    string_buffer = ''

    # Variables to indicate if we should
    # cocantenate the buffer into the final
    # text file or not

    has_user1_sent = False  # Has user1 sent a message
    has_user2_sent = False  # Has user2 returned message
    different_sender = False    # Is it a different sender now
    prev_sender = ''

    # Buffer string to be concatenated into the final string
    for match in matches:

        # match[0] - Message sender's name
        # match[1] - Message metadata (date, time)
        # match[2] - Message content (actual message)

        # Found out if the previous senders are different
        if prev_sender == match[0]:
            different_sender = False
        elif prev_sender != match[0]:
            different_sender = True

        # If it is a different sender this time and user1 and user2 has 
        # sent messages then concatenate it into the final string and
        # wipe the buffers
        if different_sender:
            if has_user1_sent and has_user2_sent:
                string_final = string_final + '\n' + string_buffer
                string_buffer = ''
                has_user1_sent = False
                has_user2_sent = False

        # Logic checking
        # Commas are removed before concatenated
        # Since our values are separated by commas
        if user1_name in match[0]:
            has_user1_sent = True
            string_buffer = string_buffer + '\n' + match[0].replace(',', '') + ',' + match[1].replace(',', '') + ',' + match[2].replace(',', '')

        elif user2_name in match[0]:
            has_user2_sent = True
            string_buffer = string_buffer + '\n' + match[0].replace(',', '') + ',' + match[1].replace(',', '') + ',' + match[2].replace(',', '')

        else:
            if user1_name not in match[0] and user2_name not in match[0]: # Must be a conversation between someone else, scrap the buffer
                string_buffer = ''
                has_user1_sent = False
                has_user2_sent = False

        # Set previous sender
        prev_sender = match[0]

        #print(match[0], match[1], match[2])

print(string_final)
