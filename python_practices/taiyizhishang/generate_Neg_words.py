#!/bin/python3

# 将文件split_test_per_add_dict.csv中emotion词前的“不”合并起来

import pandas as pd

df1 = pd.DataFrame(pd.read_csv('emotion_value_uniq.txt', header = None, sep = ','))

pos = {}
for row in range(len(df1)):
	pos[df1.ix[row, 0]] = df1.ix[row, 1]

with open('split_test_per_add_dict.csv') as f1:
	cont = f1.readlines()

W = []
for i in range(len(cont)):
#for i in range(10):
	line = (cont[i].replace('\n', '').split('\001'))
	for j in range(len(line)):
		if line[j] != '':
			w_t = [tuple(_.split(',')) for _ in line[j].split('|') if _ != '']
			W.append(w_t)

for i in range(len(W)):
	for j in range(len(W[i])):
		if W[i][j][1] == 'emotion':
			c = 0
			#for k in range(j-1, -1, -1):
			for k in range(j-1, j-2, -1):
				# 如果这个词就是第一个, 那就不往前查找了
				if k + 1 > 0:	
					if '不' in W[i][k][0]:
						if pos[W[i][j][0]] == -1:
							print(W[i][k][0] + W[i][j][0] + ',1')
						else:	
							print(W[i][k][0] + W[i][j][0] + ',-1')
						c += 1
						break
			if c == 0:
				for k in range(j+1, j+2):
					# 如果这个词就是最后一个, 那就不往后查找了
					if k - 1 < len(W[i]) - 1:
						if '不' in W[i][k][0]:
							if pos[W[i][j][0]] == -1:
								print(W[i][k][0] + W[i][j][0] + ',1')
							else:
								print(W[i][k][0] + W[i][j][0] + ',-1')			
