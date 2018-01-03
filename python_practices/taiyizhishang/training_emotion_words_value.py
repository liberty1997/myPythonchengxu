#!/bin/python3

'''
将训练集中的情感词和值取出来
'''

import pandas as pd

df = pd.DataFrame(pd.read_csv('train.csv'))
word = df['sentiment_word'].values
value  = df['sentiment_anls'].values

with open('emotion_value.txt', 'w') as fw:
	for i in range(len(word)):
		w = str(word[i]).split(';')[:-2]
		v = str(value[i]).split(';')[:-2]
		for j in range(len(w)):
			if w[j] != '' and w[j] != 'nan' and len(w[j]) > 0:
				fw.write(w[j] + ',' + v[j] + '\n')
