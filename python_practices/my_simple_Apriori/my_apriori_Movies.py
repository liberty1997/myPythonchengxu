#!/bin/python3

import pandas as pd
import copy


def Preprocess_data(fileIn, fileOut):
	
	'''
	### 以下是用文件ratings.dat生成事务数据的代码, 保存在文件Apriori_Movies_Transactions.csv中

	# 此数据集分隔符是'::', engine得是'python'
	# "the 'c' engine does not support regex separators (separators > 1 char and different from '\s+' are interpreted as regex)"
	'''

	print('Preprocessing data......')
	df = pd.DataFrame(pd.read_csv(fileIn, header = None, sep = '::', engine = 'python'))
	# 默认评分大于3的为喜欢, 仅留下大于3的数据
	data_like = df[df[2] > 3]
	# 提取用户ID
	uid = list(set(data_like[0]))
	for i in range(len(uid)):
		# 一个用户 评论的 所有的电影 作为一个事务
		transaction = sorted(list(set(data_like[data_like[0] == uid[i]][1])))
		t = pd.DataFrame({'T' : transaction})
		t.T.to_csv(fileOut, header = None, index = False, mode = 'a')

def Load_data(fname):
	
	print('Loading data......')
	transactions = []
	with open(fname) as f:
		for i in f.readlines():
			line = i.replace('\n', '').split(',')
			transactions.append(line)
	return transactions


def Find_frequent_1_itemsets(T, min_sup):
	
	'''
	扫描事务数据, 找出满足min_sup的1-频繁项集
	'''

	print('Find_frequent_1_itemsets......')
	L1 = []
	C1 = {}
	temp = []
	
	for i in range(len(T)):
		for j in range(len(T[i])):
			if T[i][j] not in C1.keys():
				C1[T[i][j]] = 0
			C1[T[i][j]] += 1
	for i in C1.items():
		if i[1] >= min_sup:
			temp.append(i[0])
	temp.sort(key = lambda a:eval(a))
	
	for i in range(len(temp)):
		t = []
		t.append(temp[i])
		L1.append(t)

	del C1, temp
	
	return L1


def Apriori_gen(K, Lk_1):
	
	'''
	生成K-频繁项集的候选集
	Lk_1 表示(K-1)-频繁项集
	'''

	print('Apriori_gen......')
	# K-频繁项集候选集
	Ck = []
	# K_1频繁项集的个数
	M = len(Lk_1)
	# 每个K_1频繁项集的项的个数, 等于 (K - 1)
	# N = len(Lk_1[0])
	N = K - 1
	# Lk_1 x Lk_1 进行连接
	for i in range(M - 1):
		for j in range(i + 1, M):
			# 若前K-2项相同, 则进行连接
			li = Lk_1[i][:-1]
			lj = Lk_1[j][:-1]
			if li == lj and (eval(Lk_1[i][-1]) < eval(Lk_1[j][-1])):
				# 若直接赋值给c, 两个变量的内存地址是一样的
				# 所以后一步执行append操作时, 就会把Lk_1也改变
				# 关于copy的知识建议自行查资料了解
				c = copy.deepcopy(Lk_1[i])
				c.append(Lk_1[j][-1])
				# 求c的子集, 进行剪枝
				subset = []
				# 轮流抽出一个元素, 剩余元素即组成子集
				for s1 in range(len(c)):
					ss = []
					for s2 in range(len(c)):
						if s1 != s2:
							ss.append(c[s2])
					subset.append(ss)
				a = 0
				# 这里子集的判断不需要issubset()函数
				for s in subset:
					if s not in Lk_1:
						a = 1
						break
				if a == 0:
					Ck.append(c)
	if len(Ck) > 0:
		return Ck
	else:
		return None


def Confidence(A, B, T):
	
	'''
	confidence(A->B) = P(B|A)
	A B 是一维列表, 表示项集
	T 表示事务
	'''
	
	print('Calculating Confidence......')
	support_count_A_B = 0
	support_count_A = 0
	for i in T:
		if set(A).issubset(set(i)):
			support_count_A += 1
		t = copy.deepcopy(A)
		for _ in B:
			t.append(_)
		if set(t).issubset(set(i)):
			support_count_A_B += 1
	confid = (support_count_A_B / support_count_A) * 100
	print('{}=>{}, confidence={}/{}={:.2f}%'.format(A, B, support_count_A_B, support_count_A, confid))
	

def Apriori_run(transactions, min_sup):
	
	print('Apriori_run......')
	# 存储所有的K-频繁项集
	Lk = []
	# 计算1-频繁项集
	L1 = Find_frequent_1_itemsets(transactions, min_sup)
	Lk.append(L1)
	# 计算2及以上频繁项集
	K = 2
	while True:
		Ck = Apriori_gen(K, Lk[K - 2])
		if Ck == None:
			break
		L = {}
		new_Lk = []
		# 对Ck中各项集的支持度进行计算及筛选
		for i in range(len(Ck)):
			for j in range(len(transactions)):
				if set(Ck[i]).issubset(set(transactions[j])):
					# 为方便使用字典, 自行设置的'key'
					key = '-'.join(Ck[i])
					if key not in L.keys():
						L[key] = 0
					L[key] += 1
		for i in L.items():
			if i[1] >= min_sup:
				new_Lk.append(i[0].split('-'))
		# 有这样的情况:
		# 能产生Ck, 但其中的项集的支持度都不满足min_sup, 同样无法产生Lk, 只能结束
		if len(new_Lk) == 0:
			break
		Lk.append(new_Lk)
		K += 1
	# 输出频繁项集
	for i in range(len(Lk)):
		print('{}项集 共{}个: {}'.format(i + 1, len(Lk[i]), Lk[i]))


if __name__ == '__main__':

	min_sup = 1250
	#dataFile = r'ratings.dat'
	preprocessResult = r'Apriori_Movies_Transactions.csv'

	# 第一次需要运行预处理数据的函数
	#Preprocess_data(dataFile, preprocessResult)
	
	# 加载数据, 运行算法
	transactions = Load_data(preprocessResult)
	Apriori_run(transactions, min_sup)
	
	# 求置信度
	A = ['1196', '1210']
	B = ['260']
	Confidence(A, B, transactions)
