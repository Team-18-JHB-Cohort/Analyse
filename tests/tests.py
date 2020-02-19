import unittest
from . import dictionary_of_metrics, five_num_summary

class Tests(unittest.TestCase):

    def test_dictionary_of_metrics(self):
        self.assertEqual(dictionary_of_metrics([1, 2, 3, 4, 5, 6]), {'mean': 3.5,
        'median': 3.5,
        'variance': 3.5,
        'standard deviation': 1.87,
        'min': 1.0,
        'max': 6.0})

    def test_five_num_summary(self):
        self.assertEqual(five_num_summary([1, 2, 3, 4, 5, 6]), {'max': 6.0, 'median': 3.5, 'min': 1.0, 'q1': 2.0, 'q3': 5.0})

    
    def extract_municipality_hashtags(self):
        self.assertEqual(extract_municipality_hashtags(df['municipality'].iloc[5,9]), ['Johannesburg', 'NaN', 'NaN','NaN']) 
        self.assertEqual(extract_municipality_hashtags(df['hashtags'].iloc[5:9]), ['NaN', ['#fridaymotivation', '#eskomexpoisf'],['#eskommpumalanga'],'NaN'])
        
    def word_splitter(self):
        self.assertEqual(word_splitter(twitter_df.copy()))
    
    def number_of_tweets_per_day(df):
        self.assertEqual(number_of_tweets_per_day(twitter_df.copy()))
