#!/bin/python3

import jieba
import re
import jieba.posseg as pseg  #标注词性
import csv

'''
对句子进行分词 词性标注
'''

#对每条text进行分词并标注词性
def cut_text_add_pseg(text):
	s=""
	data=pseg.cut(text)  #对文本进行分割
	for w in data:
		#通过合并所有中文内容得到纯中文内容
		word=''.join(re.findall(u'[\u4e00-\u9fa5]+', w.word))#去掉不是中文的内容
		word=word.strip()  #去掉字符串两端的空格
		if(len(word)!=0 and not stopwords.__contains__(word)):
			s=s+w.word+","+w.flag+"|"
	return s
def cut_text_no_pseg(text,seg=","):
	s=""
	data=jieba.cut(text)  #对文本进行分割
	for word in data:
		#通过合并所有中文内容得到纯中文内容
		word=''.join(re.findall(u'[\u4e00-\u9fa5]+', word))#去掉不是中文的内容
		word=word.strip()  #去掉字符串两端的空格
		if(len(word)!=0 and not stopwords.__contains__(word)):
			s=s+word+seg
	return s	
#对整个文件进行分词，并写入新的文件，不标注词性
def cut_words_file(textpath,savepath):
	global stopwords
	fin=open(textpath,"r",encoding="utf-8")#读取文本内容
	fout=open(savepath,'w',encoding="utf-8")#写入文本
	fwrite=csv.writer(fout)
	lines=fin.readlines()
	for data in lines:
		data=data.strip("\n")
		s=""
		text=jieba.cut(data)#分词,默认是精确分词
		for word in text:
			#通过合并所有中文内容得到纯中文内容
			#word=''.join(re.findall(u'[\u4e00-\u9fa5]+', word))#去掉不是中文的内容
			#word=word.strip()  #去掉字符串两端的空格
			if(len(word)!=0 and not stopwords.__contains__(word)):
				s=s+word+" "
		fout.write(s+"\n")
		#fout.write("\n")
		#fout.write('\n')
		#data=fin.readline()
	print(savepath+u"保存好了")
	fin.close()
	fout.close()
#对整个文件进行分词，并写入新的文件，标注词性
def cut_words_file_add_pseg(textpath,savepath):
	global stopwords
	fin=open(textpath,"rb")#读取文本内容
	fout=open(savepath,'w')
	lines=fin.readlines()
	for data in lines:
		text=pseg.cut(data)#分词,默认是精确分词
		for w in text:
			#通过合并所有中文内容得到纯中文内容
			word=w.word
			#word=''.join(re.findall(u'[\u4e00-\u9fa5]+', w.word))#去掉不是中文的内容
			#word=w.strip()  #去掉字符串两端的空格
			if(len(word)!=0 and not stopwords.__contains__(word)):
				fout.write(w.word+","+w.flag+"|")
			fout.write('\n')
	print(savepath+u"保存好了")
	fin.close()
	fout.close()

stopwords = [line.strip() for line in open('stopword1.dic',encoding="UTF-8").readlines() ]#读取中文停用词表
