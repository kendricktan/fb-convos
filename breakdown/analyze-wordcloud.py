from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import argparse
import numpy as np
import os
from PIL import Image
from os import path

# Arguements
parser = argparse.ArgumentParser(description='Generate wordcloud images from csv-formatted fb convo data')
parser.add_argument('-y', dest='year', const=2015, action='store', nargs='?', type=int, help='only display wordclouds from this year') # If year is not specify then wordcloud will be generated from everything
parser.add_argument('-s', dest='save', const='output', action='store', nargs='?', type=str, help='saves images into folder') # Saves images into folder
parser.add_argument('-m', help='mask wordcloud (to use custom masks, replace the masks with your own images)', action='store_true') # Mask images, or not
parser.add_argument('-dd', help='don\'t display wordclouds', action='store_true') # Don't display wordcloud
parser.add_argument('-ob', help='output both user\'s combined wordcloud', action='store_true') # Combine both users messages into a wordcloud too
parser.add_argument('csv', metavar='csv', type=str, help='csv file location')
args = parser.parse_args()

# Additional variables to sort out wordclouds
user1_name = '' # Variable to store user1's name
user2_name = '' # Variable to store user2's name

user1_string = '' # Variable to store messages sent by user1
user2_string = '' # Variable to store messages sent by user2

image_coloring = np.array(Image.open(path.join(path.dirname(__file__), 'mask_color.png')))

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
wordcloud_user1 = WordCloud(mask=image_coloring if args.m else None, background_color='white', max_words=2000, max_font_size=80, relative_scaling=.25).generate(user1_string)
wordcloud_user2 = WordCloud(mask=image_coloring if args.m else None, background_color='white', max_words=2000, max_font_size=80, relative_scaling=.25).generate(user2_string)
wordcloud_users = WordCloud(mask=image_coloring if args.m else None, background_color='white', max_words=2000, max_font_size=80, relative_scaling=.25).generate(user2_string + ' ' + user1_string)

# Masking colors
image_colors = ImageColorGenerator(image_coloring)

# Plot wordcloud
fig1 = plt.figure(user1_title)
plt.imshow(wordcloud_user1)
plt.axis('off')

# If mask
if args.m:
    plt.imshow(wordcloud_user1.recolor(color_func=image_colors))
    plt.axis('off')

fig2 = plt.figure(user2_title)
plt.imshow(wordcloud_user2)
plt.axis('off')

# If mask
if args.m:
    plt.imshow(wordcloud_user2.recolor(color_func=image_colors))
    plt.axis('off')

# If show combined
if args.ob:
    fig3 = plt.figure('combined wordcloud')
    plt.imshow(wordcloud_users)
    plt.axis("off")

    # If mask
    if args.m:
        plt.imshow(wordcloud_users.recolor(color_func=image_colors))
        plt.axis('off')

# Save images
if args.save:
    path_location = os.path.join(os.getcwd(), args.save)

    try:
        fig1.savefig(os.path.join(path_location, user1_title + '.jpg'))
        fig2.savefig(os.path.join(path_location, user2_title + '.jpg'))
        fig3.savefig(os.path.join(path_location, 'combined wordcloud.jpg'))

        print('Successfully written images to: ' + str(path_location))
    except:
        print('Failed to write images to: ' + str(path_location))

# Display wordclouds
if not args.dd:
    plt.show()
