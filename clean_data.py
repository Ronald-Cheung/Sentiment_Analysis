import pandas as pd
from langdetect import detect

data = pd.read_csv("twitter.csv")                                                              
filter_out = ['Category', 'keyword', 'Web_Page_URL', 'Tweet_Website', 'Author_Name', 
              'Author_Web_Page_URL', 'Tweet_Timestamp',
              'Tweet_Image_URL', 'Tweet_Video_URL', 'Tweet_Number_of_Reviews']
data.drop(columns=filter_out, inplace=True)                                                 #clean up columns                                     

#filter for english
for i, value in data['Tweet_Content'].iteritems():                                        
        lang = detect(value)                                                                    
        if lang != 'en':                                                                        
                data.drop([i], axis=0, inplace=True)                                            

data['Tweet_Content'] = data['Tweet_Content'].astype('str')                                     
data['Tweet_Times'] = pd.to_datetime(data['Tweet_Times']).dt.date                               


data.to_csv('twitter_cleaned.csv')



