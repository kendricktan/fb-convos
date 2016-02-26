## fb-convos

## About


> v1.1: Able to generate wordcloud with masks, simple by adding the -m command

>>: To use custom masks, replace the mask_color.png to the image of your choice
	
> v1.0: Able to extract conversations between two people

>>: Able to generate a wordcloud

Analayze and visualize your facebook converstaions between you and someone!

![wordcloud](http://i.imgur.com/BFvzktd.png)

## Todo
1. Message frequency according to time
2. Who initiates conversation (before and after dating)
3. Total length of messages
4. Total number of conversations against time
n. Add ability to grab messages that span over multiple lines

## Getting started
### Dependencies
matplotlib, wordcloud, ggplot is currently used to aid visualization. To install them, simple execute

    pip install matplotlib
    pip install wordcloud
    pip install ggplot

### Step 1 (Setup):
Get a copy of the repository and put the messages.htm that you downloaded from facebook into fb-convos/data/messages.htm

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
