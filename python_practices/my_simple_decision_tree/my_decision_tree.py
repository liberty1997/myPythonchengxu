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

def Load_test(fname):
	test = []
	with open(fname) as f:
		for line in f.readlines():
			test.append(line.replace('\n', '').split(' '))
	return test

def Generate_decision_tree(D, attribute_list, tree, k):
	'''
	mark == 0 返回的是类
	mark == 1 返回的是属性
	'''
	print('D===', D)
	print('path==', tree)
	D_class = {}
	for i in range(len(D)):
		if D[i][-1] not in D_class.keys():
			D_class[D[i][-1]] = 0
		D_class[D[i][-1]] += 1
	
	# D中元组同属一类
	if len(D_class) == 1:
		class_same = list(D_class)[0]
		tree.append([class_same])
		return 0, class_same
	
	# attribute_list为空时, 返回多数类
	if len(attribute_list) == 0:
		D_class = sorted(D_class.items(), key = lambda a:a[1], reverse = True)
		class_most = D_class[0][0]
		tree.append([class_most])
		return 0, class_most
	
	# 属性度量选择, 信息增益
	# 返回的N代表某个属性, 如 0 1 2 3 4 ... ...
	N = Attribute_selection_method(D, attribute_list)
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
			if D1[i][N] == N_value[nv]:
				D_split.append(D1[i])
		# 从attribute_list和D中删除属性N
		for i in range(len(attr_list)):
			if attr_list[i] == N:
				'''
				if k != 0:
					print('attr=', N + 1)
				else:
					print('attr=', N)
				'''
				for j in range(len(D1)):
					del D1[j][i]
				break
		#print('attr_list BERORE', attr_list)
		del attr_list[-1]
		#print('attr_list AFTER', attr_list)
		if len(D_split) == 0:
			class_empty = [0, D_class[0][0]]
			tree.append(class_empty)
			return 0, class_empty
		else:
			if k != 0:
				class_ = [N + 1, N_value[nv]]
				if class_ not in tree:
					tree.append(class_)
			else:
				class_ = [N, N_value[nv]]
				if class_ not in tree:
					tree.append(class_)
			Generate_decision_tree(D_split, attr_list, tree, k + 1)
	return 1, N

def Attribute_selection_method(D, attribute_list):
	# 计算哪个属性的Info最小, 即为其信息增益Gain最大
	N = 'unknown' # 返回的具有最大信息增益的属性
	min_Info = 99999
	print('attribute_list', attribute_list)
	lenD = len(D)
	'''
	if len(attribute_list) == 1:
		return attribute_list[0]
	'''
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
		print('Info_v==', Info_v)
		if Info_v < min_Info and Info_v != min_Info:
			min_Info = Info_v
			N = attribute_list[i]
	return N

def Predict(test, tree):
	for i in range(len(test)):
		pair = []
		for j in range(len(test[i])):
			pair.append([j, test[i][j]])
		print(pair)
		start = tree[0][0]
		for k in range(len(tree)):
			if tree[k][0] == start and tree[k][1] == pair[start][1]:
				start = k
				break
		while True:
			print('tree[start][0]=', tree[start][0])
			print('start=', start)
			if pair[tree[start][0]][1] == tree[start][1]:
				if len(tree[start + 1]) == 1:
					print(tree[start + 1][0])
					break
				start += 1
			else:
				start += 2

		


if __name__ == '__main__':
	D = Load_data('lenses.data.train')
	T = Load_test('my_decision_tree_test.csv')
	#D = Load_data('AllElectronics2.csv')
	#T = Load_test('AllElectronics_test.csv')
	#print('D===', D)
	#print('T===', T)
	tree = []
	# k用来标记深度. 每深入一层, 每依据一个属性划分一次,
	# attribute_list就要删去那个属性, 所以除了第一次, 其后每次输出N时都应该加1
	# k的作用: k是根据个人需要添加的!
	k = 0
	attribute_list = [ _ for _ in range(len(D[0]) - 1) ]
	Generate_decision_tree(D, attribute_list, tree, k)
	print(tree)
	Predict(T, tree)

