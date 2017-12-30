#!/bin/python3

import math
import copy

def Load_data(fname):
	data = []
	with open(fname) as f:
		for line in f.readlines():
			# 去掉每行前的编号, 仅限此数据lenses.data
			data.append(line.replace('\n', '').split(' ')[1:])
	return data

def Generate_decision_tree(D, attribute_list):
	'''
	mark == 0 返回的是类
	mark == 1 返回的是属性
	'''
	D_class = {}
	for i in range(len(D)):
		if D[i][-1] not in D_class.keys():
			D_class[D[i][-1]] = 0
		D_class[D[i][-1]] += 1
	
	# D中元组同属一类
	if len(D_class) == 1:
		print('Generate Return==0', list(D_class)[0])
		return 0, list(D_class)[0]
	
	# attribute_list为空时, 返回多数类
	if len(attribute_list) == 0:
		D_class = sorted(D_class.items(), key = lambda a:a[1], reverse = True)
		print('Generate Return==0 attrlist empty', D_class[0][0])
		return 0, D_class[0][0]
	
	# 属性度量选择, 信息增益
	# 返回的N代表某个属性, 如 0 1 2 3 4 ... ...
	N = Attribute_selection_method(D, attribute_list)
	'''
	# 从attribute_list和D中删除属性N
	for i in range(len(attribute_list)):
		if attribute_list[i] == N:
			for j in range(len(D)):
				del D[j][i]
			#del attribute_list[i]
			#break
	del attribute_list[-1]
	'''	
	N_value = set()
	for i in range(len(D)):
		N_value.add(D[i][N])
	N_value = list(N_value)
	#print('N_value=', N_value)
	for nv in range(len(N_value)):
		D_split = [] # 根据属性N的不同值, 把D划分
		D1 = copy.deepcopy(D)
		attr_list = copy.deepcopy(attribute_list)
		for i in range(len(D1)):
			#print('i=',i,' N=', N, 'nv=',nv)
			if D1[i][N] == N_value[nv]:
				D_split.append(D1[i])
		# 从attribute_list和D中删除属性N
		for i in range(len(attr_list)):
			if attr_list[i] == N:
				print('attr=', i + 1)
				for j in range(len(D1)):
					del D1[j][i]
				break
		del attr_list[-1]
		if len(D_split) == 0:
			print('Generate Return ==0 nv==', N_value[nv], D_class[0][0])
			return 0, D_class[0][0]
		else:
			print('nv=', N_value[nv])
			Generate_decision_tree(D_split, attr_list)
			print('BACK-------')
	
	print('Generate Return==1', N)
	return 1, N

def Attribute_selection_method(D, attribute_list):
	# 计算哪个属性的Info最小, 即为其信息增益Gain最大
	N = 'unknown' # 返回的具有最大信息增益的属性
	min_Info = 99999
	lenD = len(D)
	print('attribute_list', attribute_list)
	for i in range(len(attribute_list)):
		Info_v = 0.0
		attr_value = {} # 属性的值的次数
		for j in range(len(D)):
			if D[j][attribute_list[i]] not in attr_value.keys():
				attr_value[D[j][i]] = 0
			attr_value[D[j][i]] += 1
		for k in attr_value.items():
			attr_class = {} # 类别的次数
			for m in range(len(D)):
				if k[0] == D[m][attribute_list[i]]:
					if D[m][-1] not in attr_class.keys():
						attr_class[D[m][-1]] = 0
					attr_class[D[m][-1]] += 1
			temp = 0.0
			for q in attr_class.items():
				p = q[1] / k[1]
				temp += ((-p) * math.log(p, 2))
			Info_v += ((k[1] / lenD) * temp)
		if Info_v < min_Info:
			min_Info = Info_v
			N = attribute_list[i]
	#print('Attribute_selection_method:', min_Info)
	return N
				

if __name__ == '__main__':
	#D = Load_data('lenses.data')
	D = Load_data('AllElectronics.csv')
	tree = {}
	attribute_list = [ _ for _ in range(len(D[0]) - 1) ]
	Generate_decision_tree(D, attribute_list)
