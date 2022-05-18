import nltk
import pandas as pd
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()                             

data = pd.read_csv('twitter_cleaned.csv')                      #reads in the cleaned twitter csv file
data.drop(columns=data.columns[0], axis=1,inplace=True)        #drops the first column from twitter_cleaned.csv

data['Sentiment_Score'] = " "                                  #adds an empty column called Sentiment_Score to the end of dataframe 
for i, value in data['Tweet_Content'].iteritems():             #for loop to iterate through every value in the Tweet_Content column. "value" is the content at row i of the column Tweet_Content
       item = sid.polarity_scores(value)                       #Run Vader's sentiment analysis to return a dictionary of scores and store it in item
       data.at[i,'Sentiment_Score'] = item['compound']         #inserts the value associated with the dictionary key ['compound'] into the the column Sentiment_Score at row i
       

data['Result'] = " "                                           #adds an empty column called Result to the end of dataframe 
for i, value in data['Sentiment_Score'].iteritems():           #for loop to iterate through the compound scores in Sentiment_Scores column
       if value > 0:
              data.at[i, 'Result'] = "Positive"                #if the compound score is positve, insert "Positive" into the corresponding cell in new column Result
       elif value < 0:
              data.at[i, 'Result'] = "Negative"                #if the compound score is positve, insert "Negative" into the corresponding cell in new column Result
       else:
              data.drop(i,axis =0,inplace=True)                #drops row if first two conditions are not met


data.to_csv('Sentiment_Scores.csv')
