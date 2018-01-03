#!/bin/python3

import pandas as pd
import re

#df = pd.DataFrame(pd.read_csv('taiyizhishang_testset.csv', header = None))
df = pd.DataFrame(pd.read_csv('test.csv'))
#df = pd.DataFrame(pd.read_csv('test.csv'))
with open('comments_preprocessed.txt', 'w') as fw:
	#for line in df[1].values:
	for line in df['content'].values:
		fw.write(re.sub('\.|\d|，|。|！|？| |\?|!|、|;|：|；|:', '\001', str(line)) + '\n')
