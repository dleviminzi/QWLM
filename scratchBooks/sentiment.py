# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 15:38:02 2020

Basic sentiment analysis
"""

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import numpy as np

data = np.genfromtxt(r'C:\Users\Dory\Documents\GitHub\breakTheBank\data\pooled.csv', delimiter = ',', dtype= None)

#print(type(data))
#print(data.ndim)
#print(len(data))

sentences = []
stocks = []

for i in range(0, len(data)):
    sentences.append(str(data[i][6]))
    stocks.append(data[i][2])    
    
print(sentences)

analyzer = SentimentIntensityAnalyzer()
count = 0
my_tups = []

for sentence in sentences:
    vs = analyzer.polarity_scores(sentence)
    one, two, three, four = vs.items()
    txt, num = four
    
    tup = (stocks[count], num)
    my_tups.append(tup)
    
    print('\n')
    print(sentence + "   " + "Compound: " + str(num))
    
    count += 1

print(stocks)
print(my_tups)
print('\n')