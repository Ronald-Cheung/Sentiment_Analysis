import pandas as pd
from langdetect import detect

data = pd.read_csv("twitter.csv")                                                               #reads in the twitter.csv file obtained from webscraping using Octoparse
filter_out = ['Category', 'keyword', 'Web_Page_URL', 'Tweet_Website', 'Author_Name', 
              'Author_Web_Page_URL', 'Tweet_Timestamp',
              'Tweet_Image_URL', 'Tweet_Video_URL', 'Tweet_Number_of_Reviews']
data.drop(columns=filter_out, inplace=True)                                                     #drops all columns listed in filter_out

for i, value in data['Tweet_Content'].iteritems():                                              #for loop to iterate through every value in the Tweet_Content column. "value" is the content at row i of the column Tweet_Content
        lang = detect(value)                                                                    #uses langdetect library to check language of the text
        if lang != 'en':                                                                        
                data.drop([i], axis=0, inplace=True)                                            #drops entire row if language is not english

data['Tweet_Content'] = data['Tweet_Content'].astype('str')                                     #converts data in Tweet_Content to strings
data['Tweet_Times'] = pd.to_datetime(data['Tweet_Times']).dt.date                               #converts contents of Tweet_Times to show only the date


data.to_csv('twitter_cleaned.csv')



