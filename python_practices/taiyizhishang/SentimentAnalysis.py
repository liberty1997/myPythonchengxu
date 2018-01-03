#!/bin/python3
#分词的过程不加停用字典
#字典中只有训练集中的数据，没有外部的情感字典

'''
本文件分两部分运行, 第三步 是分界线
因为要用中间文件生成某些合成的情感词（负面情感词）, 更新emotion_value_uniq.txt
'''

import re
import pandas as pd
from cut_words import*   #分词工具
from tiqu_emotion_topic_n_file import*  #把分词文件中n,topic,emotion词
from  emotion_topic_by_guize import*  #提取规则

#先找到情感词，从情感词的前后去找主题词	
#第一步进行分词
'''
jieba.load_userdict('emotion_topic_uniq.dict')  #导入字典
stopwords = [line.strip() for line in open('stopword1.dic',encoding="UTF-8").readlines() ]#读取中文停用词表

fin=open("comments_preprocessed.txt")
fout=open("split_test_per_add_dict.csv","w")
lines=fin.readlines()
for line in lines:
	list1=[]
	texts=line.strip("\n").split("\001")
	for text in texts:
		words= cut_text_add_pseg(text)
		list1.append(words)
	fout.write("\001".join(list1)+"\n")
fin.close()
fout.close()

#第二步从分词中抽取出名词，主题词，情感词

openfile="split_test_per_add_dict.csv"
savefile="emotion_topic_n.csv"
emotion_topic_n(openfile,savefile)
'''

#第三步 基于规则，抽取出主题词，情感词，情感值

dict_fin=open("emotion_value_uniq.txt_uniq")
value_dict={}	
lines=dict_fin.readlines()
for line in lines:
	data=re.split(",| ",line)
	value_dict[data[0]]=data[1].strip("\n")
	

fin=open("emotion_topic_n.csv")	
fout=open("SentimentAnalysis_results.csv","w")
fout.write('row_id,content,theme,sentiment_word,sentiment_anls\n')
lines=fin.readlines()

df = pd.DataFrame(pd.read_csv('test.csv'))
comments = df['content'].values
count=1
for line in range(len(lines)):
	topic=[]
	emotion=[]
	emotion_value=[]
	new_topic=[]
	new_emotion=[]
	texts=lines[line].split("\001")
	for text in texts:
		a,b=emotion_topic_by_guize(text)
		topic.extend(a)
		emotion.extend(b)
	for i in range(len(emotion)):
		if emotion[i] in value_dict:
			new_topic.append(topic[i])
			new_emotion.append(emotion[i])
			emotion_value.append(value_dict[emotion[i]])
		
	if emotion!=[]:
		#fout.write(str(count)+",content"+","+";".join(new_topic)+";,"+";".join(new_emotion)+";,"+";".join(emotion_value)+";\n")
		fout.write(str(count) + "," + comments[line] + "," + ";".join(new_topic) + ";," + ";".join(new_emotion) + ";," + ";".join(emotion_value) + ";\n")
	else:
		#fout.write(str(count)+",content"+","+","+","+"\n")
		fout.write(str(count) + "," + comments[line] + "," + "," + "," + "\n")
	count=count+1

