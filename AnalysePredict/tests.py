#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import unittest
from . import dictionary_of_metrics, five_num_summary, five_num_summary, date_parser, extract_municipality_hashtags, number_of_tweets_per_day, word_splitter, stop_words_remover

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

    def date_parser(list_dates):
        self.assertEqual(date_parser(dates[-3:]) == ['2019-11-20', '2019-11-20', '2019-11-20'])
        
    def extract_municipality_hashtags(df):
        self.assertEqual(extract_municipality_hashtags(twitter_df.copy()))
        
    def number_of_tweets_per_day(df):
        self.assertEqual(number_of_tweets_per_day(twitter_df.copy()))
    
    def word_splitter(df):
        self.assertEqual(word_splitter(twitter_df.copy()))
    
    def stop_words_remover(df):
        self.assertEqual(stop_words_remover(twitter_df.copy()).loc[0, "Without Stop Words"], ['@bongadlulane', 'send', 'email', 'mediadesk@eskom.co.za'])

