import nltk
import pandas as pd
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()                             

data = pd.read_csv('twitter_cleaned.csv')                     
data.drop(columns=data.columns[0], axis=1,inplace=True)        


#run VADER to get compound sentiment score
data['Sentiment_Score'] = " "                                  
for i, value in data['Tweet_Content'].iteritems():              
       item = sid.polarity_scores(value)                       
       data.at[i,'Sentiment_Score'] = item['compound']         
       
#Organize scores       
data['Result'] = " "                                           
for i, value in data['Sentiment_Score'].iteritems():           
       if value > 0:
              data.at[i, 'Result'] = "Positive"                
       elif value < 0:
              data.at[i, 'Result'] = "Negative"                
       else:
              data.drop(i,axis =0,inplace=True)                


data.to_csv('Sentiment_Scores.csv')
