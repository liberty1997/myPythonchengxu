#! -*- coding:utf-8 -*-
#把文本中所有标注topic和emotion的词抽取出来
def emotion_topic_n(openfile,savefile):
	fin=open(openfile)
	fout=open(savefile,"w")
	lines=fin.readlines()
	for line in lines:
		segs=line.split("\001")
		for seg in segs:
			words=seg.split("|")
			for i in range(len(words)-1):
				word=words[i].split(",")[0]
				pseg=words[i].split(",")[1]
				if (pseg=="topic") or (pseg=="emotion")or(pseg=="n") or (pseg=="a"):
					fout.write(words[i]+"|")
			fout.write("\001")
		fout.write("\n")