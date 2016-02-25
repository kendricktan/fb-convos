from wordcloud import WordCloud
import argparse
import re
import htmllib

# Escaping html so we don't have messages like
# &amp, &quot, &gt, etc...
def html_escape(s):
    p = htmllib.HTMLParser(None)
    p.save_bgn()
    p.feed(s)
    return p.save_end()

# Command line arguements
parser = argparse.ArgumentParser(description='Extract and format fb messages to be analyzed, with some simple wordclouds and statistics')
parser.add_argument('infile', metavar='if', type=str, help='in-file location')
parser.add_argument('outfile', metavar='of', type=str, help='out-file location')
parser.add_argument('user1', metavar='u1', type=str, help='User 1\'s name within the conversation')
parser.add_argument('user2', metavar='u2', type=str, help='User 2\'s name within the conversation')
parser.add_argument('-v', help='increase output verbosity', action='store_true')
parser.add_argument('-s', help='display message statistics', action='store_true')
parser.add_argument('-wc', help='display simple wordcloud', action='store_true')
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

# Our total user messages
messages_total = ''
user1_messages_total = ''
user2_messages_total = ''

# Message statistics
total_messages_sent = 0
user1_messages_sent = 0
user2_messages_sent = 0
user1_temp_messages = 0
user2_temp_messages = 0

################################ RULES #######################################
#                                                                            #
# > Conversation will be considered initiated if there isn't any previous    #
# conversation between the two for 15 minutes                                #
#                                                                            #
# > Since facebook organizes the message really untidily, it'll only extract #
# messages which you (user 1) initiate, and which user 2 ends with or        #
# continue, or vice-versa                                                    #
#                                                                            #
##############################################################################

############# CSV Format ################
# Sender, Day, Date, Time, UTC, Message #
#########################################

for raw_line in raw_msg_file:
    # Find regular expression
    matches = re.findall(regex_exp, raw_line)

    # String buffer to be concatentated
    # with relavent information
    string_buffer = ''

    # Variables to indicate if we should
    # cocantenate the buffer into the final
    # text file or not

    has_user1_sent = False  # Has user1 sent a message
    has_user2_sent = False  # Has user2 returned message
    different_sender = False    # Is it a different sender now
    prev_sender = ''        # Who was the previous sender

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

                # If verbose
                if args.v:
                    print(string_buffer)

                # Writes to file
                fmt_msg_file.write(string_buffer)

                # If want statistics then we append to final string
                if args.s:
                    user1_messages_sent = user1_messages_sent + user1_temp_messages
                    user2_messages_sent = user2_messages_sent + user2_temp_messages
                    user1_temp_messages = 0
                    user2_temp_messages = 0

                # Appends message information to
                # respective senders
                for csv_split in string_buffer.split('\n'):
                    lines_splitted = csv_split.split(',')

                    # lines_splitted[0] = sender name
                    # lines_splitted[1] = day
                    # lines_splitted[2] = date
                    # lines_splitted[3] = time
                    # lines_splitted[4] = UTC
                    # lines_splitted[5] = message

                    # Don't want it to crash
                    try:
                        # Append it to our messages
                        messages_total = messages_total + ' ' + lines_splitted[5]

                        if user1_name in lines_splitted[0]:
                            user1_messages_total = user1_messages_total + ' ' + lines_splitted[5]
                        elif user2_name in lines_splitted[0]:
                            user2_messages_total = user2_messages_total + ' ' + lines_splitted[5]

                    except:
                        pass


                # Resets the values
                string_buffer = ''
                has_user1_sent = False
                has_user2_sent = False

        # Logic checking
        # Commas are removed before concatenated
        # Since our values are separated by commas

        if user1_name in match[0]:
            # User statistics
            if args.s:
                user1_temp_messages = user1_temp_messages + 1

            # Logic checking
            has_user1_sent = True

            # Datetime formatted CSV
            datetime_buffer = match[1].replace(',', '').split()

            string_buffer = string_buffer + '\n' + match[0].replace(',', '') + ',' + datetime_buffer[0] + ',' + datetime_buffer[1] + ' ' + datetime_buffer[2] + ' ' + datetime_buffer[3] + ',' + datetime_buffer[5] + ',' + datetime_buffer[6] + ',' + html_escape(match[2].replace(',', ''))

        elif user2_name in match[0]:
            # User statistics
            if args.s:
                user2_temp_messages = user2_temp_messages + 1

            # Logic checking
            has_user2_sent = True

            # Datetime formatted CSV
            datetime_buffer = match[1].replace(',', '').split()

            string_buffer = string_buffer + '\n' + match[0].replace(',', '') + ',' + datetime_buffer[0] + ',' + datetime_buffer[1] + ' ' + datetime_buffer[2] + ' ' + datetime_buffer[3] + ',' + datetime_buffer[5] + ',' + datetime_buffer[6] + ',' + html_escape(match[2].replace(',', ''))

        else:
            if user1_name not in match[0] and user2_name not in match[0]: # Must be a conversation between someone else, scrap the buffer
                string_buffer = ''
                has_user1_sent = False
                has_user2_sent = False
                user1_temp_messages = 0
                user2_temp_messages = 0

        # Set previous sender
        prev_sender = match[0]

# Close files
raw_msg_file.close()
fmt_msg_file.close()

# Display wordcloud
if args.wc:
    # Generate wordcloud
    wordcloud = WordCloud().generate(messages_total)

    # Display a wordcloud image
    # the matplotlib way:
    import matplotlib.pyplot as plt
    plt.imshow(wordcloud)
    plt.axis("off")

    wordcloud = WordCloud(max_font_size=40, relative_scaling=.5).generate(messages_total)
    plt.figure()
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

# User statistics
if args.s:
    print("#### Statistics ####")
    print("total_messages_sent: " + str(user1_messages_sent + user2_messages_sent))
    print("user1_messages_sent: " + str(user1_messages_sent))
    print("user2_messages_sent: " + str(user2_messages_sent))
