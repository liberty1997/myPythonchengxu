#!/bin/python3

import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np

'''
基于邻近性（距离）的离群点检测
'''

def Load_data(fname, idx):
	'''
	假定测试数据为data1.mat data2.mat
	'''
	data = sio.loadmat(fname)[idx]
	D = []
	for i in range(len(data)):
		temp = []
		for j in range(len(data[i])):
			temp.append(data[i][j])
		D.append(temp)
	return D

def OutLierDetection(D, r, f):
	'''
	r表示距离阈值
	f表示分数阈值
	'''
	OutLiers = []
	lenD = len(D)
	for i in range(lenD):
		count = 0
		mark = 0
		DIS = 0.0
		for j in range(lenD):
			DIS += np.linalg.norm(np.array(D[i]) - np.array(D[j]))
		DIS = (DIS / lenD)
		for j in range(lenD):
			if i != j:
				dis = np.linalg.norm( np.array(D[i]) - np.array(D[j]) )
				if dis <= DIS:
					count += 1
					if count >= (f * lenD):
						mark = 1
						break
		if mark == 0:
			OutLiers.append(D[i])
	return OutLiers

if __name__ == '__main__':
	D = Load_data('data1.mat', 'X')
	# 这俩参数是data1.mat的
	OutLiers = OutLierDetection(D, 10, 0.5342047520)
	print((OutLiers))

	X = []
	Y = []
	x1 = []
	y1 = []
	fig = plt.figure()
	ax1 = fig.add_subplot(111)
	for i in range(len(D)):
		if D[i] not in OutLiers:
			X.append(D[i][0])
			Y.append(D[i][1])
		else:
			x1.append(D[i][0])
			y1.append(D[i][1])
	ax1.scatter(X, Y, c = 'g')
	# 离群点用红色表示
	ax1.scatter(x1, y1, c = 'r')
	plt.show()
