#!/bin/python3
#分词的过程不加停用字典
#字典中只有训练集中的数据，没有外部的情感字典
import re

def emotion_topic_by_guize(text):
	words=text.split("|")
	topic=[]
	emotion=[]
	#当数据长度大于3时
	#1）如果第一个词为情感词，则判断其后的词是否为主题词，若为主题词，则[主题词、情感词]，若无则[NULL,情感词]
	#2)如果第二个词开始之后到最后一个词之前的词为情感词，则判断其前、后一个是否为主题
	#3）如果最后一个词为情感词,则判断其前1个是否为情感词
	if len(words)-1>=3:
		for i in range(len(words)-1):
			if i==0 :
				word=words[i].split(",")
				behind_word=words[i+1].split(",")
				if (word[1]=="emotion" or word[1]=="a") and (behind_word[1]!="topic" and behind_word[1]!="n" ):
					emotion.append(word[0])
					topic.append("NULL")
				if (word[1]=="emotion" or word[1]=="a") and (behind_word[1]=="topic" or behind_word[1]=="n"):
					emotion.append(word[0])
					topic.append(behind_word[0])
			if i>=1 and i<len(words)-2:
				word=words[i].split(",")
				pre_word=words[i-1].split(",")
				behind_word=words[i+1].split(",")
				if word[1]=="emotion" or word[1]=="a":
					if (pre_word[1]=="topic" or pre_word[1]=="n") and (behind_word[1]!="topic" and behind_word[1]!="n"):
						topic.append(pre_word[0])
						emotion.append(word[0])
					if (pre_word[1]!="topic" and pre_word[1]!="n") and (behind_word[1]=="topic" or behind_word[1]=="n") :
						topic.append(behind_word[0])
						emotion.append(word[0])
					else:
						emotion.append(word[0])
						topic.append("NULL")
			if i==len(words)-2:
				word=words[i].split(",")
				pre_word=words[i-1].split(",")
				if (word[1]=="emotion" or word[1]=="a") and (pre_word[1]=="topic" or pre_word[1]=="n"):
					emotion.append(word[0])
					topic.append(pre_word[0])
				if (word[1]=="emotion" or word[1]=="a") and (pre_word[1]!="topic" and pre_word[1]!="n"):
					emotion.append(word[0])
					topic.append("NULL")
	if len(words)-1==1:
		word=words[0].split(",")
		if word[1]=="emotion" or word[1]=="a" :
			emotion.append(word[0])
			topic.append("NULL")
	#如果句中有两个词
	if len(words)-1==2:
		word0=words[0].split(",")
		word1=words[1].split(",")
		if (word0[1]=="emotion" or word0[1]=="a") and (word1[1]=="topic" or word1[1]=="n"):
			emotion.append(word0[0])
			topic.append(word1[0])
		if (word1[1]=="emotion" or word1[1]=="a") and (word0[1]=="topic" or word0[1]=="n"):
			emotion.append(word1[0])
			topic.append(word0[0])
		if (word1[1]=="emotion" or word1[1]=="a") and (word0[1]!="topic" and word0[1]!="n"):
			emotion.append(word1[0])
			topic.append("NULL")
		if (word0[1]=="emotion"  or word0[1]=="a" )and (word1[1]!="topic" and word1[1]!="n"):
			emotion.append(word0[0])
			topic.append("NULL")
			
	return topic,emotion
"""
text="排版,topic|有问题,emotion|字,n|看不到,emotion|"
words=text.split("\001")
for word in words:
	topic,emotion=emotion_topic_by_guize(word)
	print(topic,emotion)
"""	

"""
dict_fin=open("emotion_value_uniq.csv",encoding="utf-8")
value_dict={}	
lines=dict_fin.readlines()
for line in lines:
	data=re.split(",| ",line)
	value_dict[data[0]]=data[1].strip("\n")
	

#fin=open("topic_emotion.csv")	
fin=open("new_n_topic_emotion.csv")	
fout=open("new_n_topic_emotion_value_v2.csv","w")
lines=fin.readlines()

i=1
for line in lines:
	topic=[]
	emotion=[]
	texts=line.split("\001")
	for text in texts:
		a,b=emotion_topic_by_guize(text)
		topic.extend(a)
		emotion.extend(b)
	if emotion!=[]:
		fout.write(str(i)+",content"+","+";".join(topic)+";,"+";".join(emotion)+";,"+";".join([value_dict[word] for word in emotion])+";\n")
	else:
		fout.write(str(i)+",content"+","+","+","+"\n")
	i=i+1
"""
