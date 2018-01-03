#!/bin/python3

'''
提取出来训练集中的主题词和情感词, 将其做成自定义字典
'''

import pandas as pd

df = pd.DataFrame(pd.read_csv('train.csv'))

theme = df['theme'].values
word = df['sentiment_word'].values

with open('emotion_topic.dict', 'w') as fw:
	for i in range(len(theme)):
		t = str(theme[i]).split(';')[:-2]
		w = str(word[i]).split(';')[:-2]
		for j in range(len(t)):
			fw.write(t[j] + ' 345 ' + 'topic' + '\n')
			fw.write(w[j] + ' 345 ' + 'emotion' + '\n')
