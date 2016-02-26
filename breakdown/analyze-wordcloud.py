from wordcloud import WordCloud
import matplotlib.pyplot as plt
import argparse

# Arguements
parser = argparse.ArgumentParser(description='Generate wordcloud images from csv-formatted fb convo data')
parser.add_argument('-y', dest='year', const=2015, action='store', nargs='?', type=int, help='only display wordclouds from this year') # If year is not specify then wordcloud will be generated from everything
parser.add_argument('-ob', help='output both user\'s combined wordcloud', action='store_true') # Combine both users messages into a wordcloud too
parser.add_argument('csv', metavar='csv', type=str, help='csv file location')
parser.add_argument('ol', metavar='ol', type=str, help='output FOLDER location')
args = parser.parse_args()

# Additional variables to sort out wordclouds
user1_name = '' # Variable to store user1's name
user2_name = '' # Variable to store user2's name

user1_string = '' # Variable to store messages sent by user1
user2_string = '' # Variable to store messages sent by user2

# Opens csv file (comma separated values: csv)
with open(args.csv, 'rb') as f:
    for line in f.readlines():
        csv_vals = line.split(',')

        try:
            temp = csv_vals[5]
        except:
            continue

        # csv_vals[0] = Sender name
        # csv_vals[1] = Day
        # csv_vals[2] = Date
        # csv_vals[3] = Time
        # csv_vals[4] = UTC
        # csv_vals[5] = Message

        # Check names and adds messages sent
        # to a variable respectively
        if user1_name == '':
            user1_name = csv_vals[0]
        elif user2_name == '':
            if csv_vals[0] != user1_name:
                user2_name = csv_vals[0]

        # If it wants a specific year
        if args.year:
            if str(args.year) in csv_vals[2]:
                # Add messages according to user
                if csv_vals[0] == user1_name:
                    user1_string = user1_string + ' ' + csv_vals[5]
                else:
                    user2_string = user2_string + ' ' + csv_vals[5]

        else:
            if csv_vals[0] == user1_name:
                user1_string = user1_string + ' ' + csv_vals[5]
            else:
                user2_string = user2_string + ' ' + csv_vals[5]


# Wordcloud title
user1_title = user1_name + '\'s ' + (str(args.year) if args.year else '') + ' wordcloud' # Variable to store user1's plot title
user2_title = user2_name + '\'s ' + (str(args.year) if args.year else '') + ' wordcloud' # Variable to store user2's plot title

# Generate wordcloud
wordcloud_user1 = WordCloud(background_color='white', max_words=2000, max_font_size=80, relative_scaling=.25).generate(user1_string)
wordcloud_user2 = WordCloud(background_color='white', max_words=2000, max_font_size=80, relative_scaling=.25).generate(user2_string)
wordcloud_users = WordCloud(background_color='white', max_words=2000, max_font_size=80, relative_scaling=.25).generate(user2_string + ' ' + user1_string)

# Plot wordcloud
plt.figure(user1_title)
plt.imshow(wordcloud_user1)
plt.axis('off')

plt.figure(user2_title)
plt.imshow(wordcloud_user2)
plt.axis('off')

plt.figure('combined WordCloud')
plt.imshow(wordcloud_users)
plt.axis('off')
plt.show()
