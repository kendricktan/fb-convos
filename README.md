## fb-convos

## About

#### 06/03/2016:

Made graphs a little bit more prettier, also added the option to display stats from users on the graph (not shown in pic)

![graph-pretty](http://i.imgur.com/peSuq3S.png)

Able to generate basic pie charts to demonstrate the chat distribution across the days

![pie-chart](http://i.imgur.com/wLRL5tU.png)

#### 05/03/2016:

Able to generate basic graphs that depict the messaging frequency over time

![freq-graph](http://i.imgur.com/QOnModk.png)

#### 26/02/2016:

Able to generate wordcloud with masks, simple by adding the -m flag

To use custom masks, replace the mask_color.png in the breakdown folder to the image of your choice
 
![wordcloud-masked](http://i.imgur.com/NFZnilS.png)

#### 25/02/2016: 

 Able to extract conversations between two people

 Able to generate a wordcloud

Analayze and visualize your facebook converstaions between you and someone!

![wordcloud](http://i.imgur.com/BFvzktd.png)

## Todo
1. Message frequency according to time (pie chart of which days you talk the most) [blue=you, red=her, green=all]
2. Who initiates conversation 
3. Mouse click events for the graphs 

## Getting started
### Dependencies
matplotlib, wordcloud, ggplot is currently used to aid visualization. To install them, simple execute

    pip install matplotlib
    pip install wordcloud
    pip install seaborn

### Step 1 (Setup):
Get a copy of the repository and put the messages.htm that you downloaded from facebook into fb-convos/data/messages.htm. For more info on downloading your facebook data goto https://www.facebook.com/help/131112897028467/

    git clone https://github.com/kendricktan/fb-convos.git
    cd fb-convos
    cp [your messages.htm location here] data/messages.htm
	
### Step 2 (Formatting):
Before doing anything we first need to extract information from the downloaded message data dump (aka messages.htm)

    python breakdown/extract.py data/messages.htm data/out.csv [User1's name] [User2's name]
	
If you want a simple wordcloud generated whilst formatting it, simply add the -wc flag

    python breakdown/extract.py -wc data/messages.htm data/out.csv [User1's name] [User2's name]
    
For more information simply invoke the --help flag

    python breakdown/extract.py --help
    
### Step 3 (Wordcloud):
To generate a wordcloud from add the formatted data, simply invoke

    python breakdown/analyze-wordcloud.py data/out.csv

For wordcloud which combines messages from both users simply invoke the `-ob` (output both) flag

    python breakdown/analyze-wordcloud.py -ob data/out.csv

To specify a specific year (for example, 2014) do:

    python breakdown/analyze-wordcloud.py -y 2014 data/out.csv 
    
To generate a masked wordcloud (with the default image of a cat), run:
    
    python breakdown/analyze-wordcloud.py -m data/out.csv 

To save the files and don't display the masked wordclouds, run:

    python breakdown/anaylze-wordcloud.py -m -dd -s [FOLDER LOCATION] data/out.csv

Again, for more information invoke the --help flag
    
    python breakdown/analyze-wordcloud.py --help

### Step 4 (message frequency against time in a graph form)
To generate a graph of the message frequency against time, simply invoke

    python breakdown/analyze-msg-freq-grah.py data/out.csv

To specify a start date for the graph (forcefully start displaying from that date), simply invoke the `-sd` (start date) flag

#### the -sd flag format is [YYYY-MM-DD] 

    python breakdown/analyze-msg-freq-grah.py -sd 2015-09-20 data/out.csv

To specify a end date for the graph (forcefully display until that date), simply invole the `-ed` (end date) flag

#### the -ed flag format is [YYYY-MM-DD]

    python breakdown/analyze-msg-freq-grah.py -sd 2015-09-20 -ed 2016-01-01 data/out.csv

To display all graphs (a.k.a graphs from user1 and user2), add the -da flag

    python breakdown/analyze-msg-freq-grah.py -da -sd 2015-09-20 -ed 2016-01-01 data/out.csv

To manually specify a user's name user the -u1 or -u2 command (for the -da output), e.g.

    python breakdown/analyze-msg-freq-grah.py -u1 USER1 -u2 USER2 -sd 2015-09-20 -ed 2016-01-01 data/out.csv

### Step 5 (chat distribution in a pie chart)
To generate a pie chart of the distribution of chat across the days, simply invoke

    python breakdown/analyze-msg-daily-piechart.py data/out.csv

