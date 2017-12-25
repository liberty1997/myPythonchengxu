#!/bin/python3

import numpy as np
import matplotlib.pyplot as plt

def Load_data(fname):
	with open(fname) as f:
		con = f.readlines()
	data = []
	for lines in con:
		p = []
		line = lines.replace('\n', '').split('\t')
		for i in range(len(line)):
			p.append(float(line[i]))
		data.append(p)
	return data


def Reallocate(XX, C):
	'''
	接收簇, 然后返回重新分配后的簇
	'''
	k = len(XX)
	C_new = [ [] for _ in range(k) ]
	for c in range(len(C)):
		for j in range(len(C[c])):
			min = 99999
			mark = -1
			for i in range(k):
				p1 = np.array(XX[i])
				p2 = np.array(C[c][j])
				EM = np.linalg.norm(p2 - p1)
				if EM < min:
					min = EM
					mark = i
			C_new[mark].append(C[c][j])
	return C_new
		

def ReCalcMean(C):
	'''
	计算每个簇的形心(均值)
	返回形心列表
	'''
	k = len(C)
	XingXin = []
	for i in range(k):
		XX = [ 0 for _ in range(len(C[0][0])) ]
		n = len(C[i])
		for j in range(n):
			for x in range(len(XX)):
				XX[x] += C[i][j][x]
		XX = [ _ / n for _ in XX]
		XingXin.append(XX)
	return XingXin

def Fig(C, k, count):
	'''
	这里画散点图, 默认二维
	三维以上, 后续再画
	'''
	#k = len(C) # 簇的个数
	k = k
	color = ['b', 'c', 'g', 'k', 'm', 'r', 'w', 'y']
	
	fig = plt.figure()
	ax1 = fig.add_subplot(111)
	
	for i in range(k):
		P = [ [] for _ in range(len(C[i][0]))]
		for j in range(len(C[i])):
			for p in range(len(C[i][0])):
				P[p].append(C[i][j][p])
		ax1.scatter(P[0], P[1], c = color[i])
		plt.savefig('my_k_means_fig_' + str(count) + '.png')

if __name__ == '__main__':
	k = int(input('Please input an integer as k: '))
	d = [ _ for _ in Load_data('data1.txt') ]
	#d = [ _ for _ in Load_data('data2.txt') ]
	D = [ d ] # 设初始数据同属一个簇
	XingXin = [] # 形心
	for i in range(k):
		XingXin.append(D[0][np.random.randint(len(D[0]))])
	# 对初始簇进行第一次划分, 而形心使用的是随即形心, 故称'Round 0'
	print('\nRound 0 XingXin:', XingXin)
	C = Reallocate(XingXin, D)
	count = 0
	Fig(C, k, count)
	while True:
		XingXin = ReCalcMean(C)
		C_new = Reallocate(XingXin, C)
		Fig(C, k, count + 1)
		print('Round {} XingXin: {}'.format(count + 1, XingXin))
		if C_new == C:
			break
		else:
			C = C_new
			count += 1
