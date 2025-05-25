#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 12:24:06 2020

@author: milad
"""

import codecs, json
import os
import pandas as pd 
import nltk
import gensim
from gensim import corpora, models, similarities


   
df1 = pd.read_json('/home/milad/python projects/twittercrawler/fa1tweetes.json', encoding='utf-8')
df2 = pd.read_json('/home/milad/python projects/twittercrawler/tweetseuro20142020.json', encoding='utf-8')
df3 = pd.read_json('/home/milad/python projects/twittercrawler/tweetsfararu20142020.json', encoding='utf-8')
df4 = pd.read_json('/home/milad/python projects/twittercrawler/tweetstabnak20142020.json', encoding='utf-8')
df5 = pd.read_json('/home/milad/python projects/twittercrawler/tweetsisna20142020.json', encoding='utf-8')
df6 = pd.read_json('/home/milad/python projects/twittercrawler/tweetsdeghtesad20142020.json', encoding='utf-8')
df7 = pd.read_json('/home/milad/python projects/twittercrawler/tweetsbbc20142020.json', encoding='utf-8')
df8 = pd.read_json('/home/milad/python projects/twittercrawler/tweets7sobh20142020.json', encoding='utf-8')

df = []


df.extend(df1["text"])
df.extend(df2["text"])
df.extend(df3["text"])
df.extend(df4["text"])
df.extend(df5["text"])
df.extend(df6["text"])
df.extend(df7["text"])
df.extend(df8["text"])



print(len(df))


tok_corp = [nltk.word_tokenize(sent) for sent in df]
model = gensim.models.Word2Vec(tok_corp, min_count= 2, size = 100)
model.save('/home/milad/python projects/model/test1model')

