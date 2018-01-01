#!/bin/python3

import math
import copy

def Load_data(fname):
	data = []
	with open(fname) as f:
		con = f.readlines()
		for line in range(len(con)):
			# 去掉每行前的编号, 仅限此数据lenses.data
			data.append(con[line].replace('\n', '').split(' ')[1:])
	return data

def Load_test(fname):
	test = []
	with open(fname) as f:
		con = f.readlines()
		for line in range(len(con)):
			test.append(con[line].replace('\n', '').split(' '))
	return test

def Generate_decision_tree(D, attribute_list, tree):
	'''
	mark == 0 返回的是类
	mark == 1 返回的是属性
	'''
	D_class = {}
	print('tree==', tree)
	print('D==', D)
	# D中每条的类别计数 排序 找多数类
	for i in range(len(D)):
		if D[i][-1] not in D_class.keys():
			D_class[D[i][-1]] = 0
		D_class[D[i][-1]] += 1
	D_class = sorted(D_class.items(), key = lambda a:a[1], reverse = True)
	
	# D中元组同属一类
	if len(D_class) == 1:
		class_same = D_class[0][0]
		tree.append([class_same])
		return 0, class_same
	
	# attribute_list为空时, 返回多数类
	if len(attribute_list) == 0:
		class_most = D_class[0][0]
		tree.append([class_most])
		return 0, class_most
	
	# 属性度量选择, 信息增益
	# 返回的N代表某个属性, 如 0 1 2 3 4 ... ...
	N = Attribute_selection_method(D, attribute_list)
	print('N==', N)
	N_value = set()
	for i in range(len(D)):
		N_value.add(D[i][N])
	N_value = list(N_value)
	attr_list = copy.deepcopy(attribute_list)
	del attr_list[-1]
	for nv in range(len(N_value)):
		D_split = [] # 根据属性N的不同值, 把D划分
		for i in range(len(D)):
			if D[i][N] == N_value[nv]:
				D_split.append(D[i])
		if len(D_split) == 0:
			class_empty = [D_class[0][0]]
			tree.append(class_empty)
			return 0, class_empty
		else:
			class_ = [N, N_value[nv]]
			tree.append(class_)
			Generate_decision_tree(D_split, attr_list, tree)
	return 1, N

def Attribute_selection_method(D, attribute_list):
	# 计算哪个属性的Info最小, 即为其信息增益Gain最大
	N = 'unknown' # 返回的具有最大信息增益的属性
	min_Info = 99999
	lenD = len(D)
	if len(attribute_list) == 1:
		# 属性列表仅剩一个时, 直接输出其划分属性, 就一个属性了, 没必要计算
		# 经观察, 这里加1, 就不会出错了......
		return attribute_list[0] + 1
	
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
		if Info_v < min_Info and Info_v != min_Info:
			min_Info = Info_v
			N = attribute_list[i]
	return N

def Predict(test, tree):
	for i in range(len(test)):
		pair = []
		attr = tree[0][0] # 每条测试集的属性的标记
		attr_prev = -1 # 记录前一个结点的属性号
		t = 0
		for j in range(len(test[i])):
			if j == attr:
				t = 1
			pair.append([j, test[i][j]])
		# 根结点的属性不在test[i]的属性中, 直接输出unknown
		if t == 0:
			print('unknown 1')
			continue
		mark = 1
		tree_pos = 0 # tree上的标记
		# 按树的路径, 找出符合的最终类别
		while mark:
			# 找到了类别
			if len(tree[tree_pos]) == 1:
				print(tree[tree_pos][0])
				mark = 0
				break

			# 如果匹配当前结点, 则继续按深度找下去
			# 如果匹配不上, 则需要搜索其它分枝
			if tree[tree_pos] == pair[attr]:
				attr_prev = copy.deepcopy(attr)
				tree_pos += 1
				if len(tree[tree_pos]) > 1:
					#attr_prev = copy.deepcopy(attr)
					attr = tree[tree_pos][0]
			else:
				# 先确定一下搜索范围
				find = -1
				for j in range(tree_pos + 1, len(tree)):
					#attr_prev = copy.deepcopy(attr)
					if len(tree[j]) > 1:
						#print('j + 1==', j + 1, 'attr_prev', attr_prev)
						#print('tree['+str(j)+'][0]', tree[j][0], ' attr_prev', attr_prev)
						if tree[j][0] == attr_prev:
							find = j + 1
							break
				if find == -1:
					find = len(tree)
				mm = 0
				#print('find ', find)
				for j in range(tree_pos + 1, find):
					if len(tree[j]) > 1:
						if tree[j] == pair[attr]:
							tree_pos = j
							#print('tree_pos==', tree_pos)
							#tree_pos = j + 1
							#attr_prev = copy.deepcopy(attr)
							#attr = tree[tree_pos][0]
							mm = 1
							break
				if mm == 0:
					print('unknown 2')
					mark = 0

if __name__ == '__main__':
	D = Load_data('lenses.data.train')
	T = Load_test('my_decision_tree_test.csv')
	#D = Load_data('AllElectronics2.csv')
	#T = Load_test('AllElectronics_test.csv')
	tree = []
	attribute_list = [ _ for _ in range(len(D[0]) - 1) ]
	Generate_decision_tree(D, attribute_list, tree)
	print('my Decision Tree:\n', tree)
	print('Predict:')
	Predict(T, tree)
