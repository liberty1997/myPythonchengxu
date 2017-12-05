#!/bin/python3

import pandas as pd

def load_data(f, sep = ' '):
	return pd.DataFrame(pd.read_csv(f, header = None, sep = sep))

def find_frequent_1_itemsets(D):
	'''
	扫描数据，找出1频繁项集，剔除不满足最小支持度（min_sup）的项
	'''
	C1 = {}
	L1 = {}
	items = []
	# 求各项的支持度，做字典映射
	for i in range(len(D)):
		item = D[i].split(',')
		for it in item:
			if it not in C1.keys():
				C1[it] = 0
			C1[it] += 1
			if it not in items:
				items.append(it)
	# 排序 剔除不满足（min_sup）项
	items.sort()
	for i in range(len(items)):
		if C1[items[i]] >= min_sup:
			L1[items[i]] = C1[items[i]]
	del C1, items
	return L1
	
def apriori_gen(K, Lk_1):
	'''
	生成候选集 | 连接 剪枝
	参数1 表示求K项集， 参数2 表示K-1频繁项集
	'''
	# Ck保存K频繁项集的候选集
	Ck = []
	# Lk 和 Lk 作连接 （Lk x Lk）
	# 默认Lk的元素是有序的，'I1' 'I2' 'I3' ......
	# 所以连接的结果有 (len(Lk) * (len(Lk) - 1)) / 2 个
	for i in range(len(Lk_1) - 1):
		for j in range(i + 1, len(Lk_1)):
			c = []
			# 假设l1与l2作连接
			# 判断l1与l2第1个元素至倒数第二个元素是否都相等
			a = 0
			for ii in range(len(Lk_1[0]) - 1):
				if Lk_1[i][ii] != Lk_1[j][ii]:
					a = 1
			# 如果都相等，就将l1的全部元素和l2的最后一个元素作为一个结果（K频繁项集的候选项）
			if a == 0 and Lk_1[i][len(Lk_1[0]) - 1] < Lk_1[j][len(Lk_1[0]) - 1]:
				for t in range(len(Lk_1[0])):
					c.append(Lk_1[i][t])
				c.append(Lk_1[j][len(Lk_1[0]) - 1])
				c = list(set(c))
				c.sort()
				# 进行剪枝 求子集
				# 如果候选集的子集有不是K-1项频繁项集的，那就舍弃此候选项
				# 因为这里候选集的子集肯定比候选集少一个元素，所以轮流拿出一个元素，剩下的就是子集
				subset = []
				for s1 in range(len(c)):
					ss = []
					for s2 in range(len(c)):
						if s1 != s2: 
							ss.append(c[s2])
					subset.append(ss)
				del ss
				a = 0
				for su in subset:
					if su not in Lk_1:
						a = 1
						break
				# 只有这个候选项的子集都是频繁项集，才将此项加入候选集
				if a == 0:
					Ck.append(c)
			del c
	# 若无频繁项集候选集，返回None
	if len(Ck) == 0:
		return None
	else:
		return Ck

if __name__ == '__main__':

	# 最小支持度
	min_sup = 2
	data = load_data('apriori_data.csv', sep = ' ')
	# 保存原始事务
	itemsets = []
	for i in range(len(data[1])):
		ii = data[1][i].split(',')
		itemsets.append(ii)
	# 求1频繁项集
	L1 = find_frequent_1_itemsets(data[1])
	Lk = []
	l = []
	for i in L1.items():
		ll = []
		ll.append(i[0])
		l.append(ll)
	Lk.append(l)
	del l

	k = 2
	while Lk[k - 2]:
		# 求2及以上的频繁项集
		Ck = apriori_gen(k, Lk[k - 2])
		# 若没有候选集，则表明所有频繁项集已找到
		if Ck == None:
			break
		# 找到候选集后，求出支持度
		L2 = {}
		for j in range(len(Ck)):
			for i in range(len(itemsets)):
				if set(Ck[j]).issubset(set(itemsets[i])):
					key = ''.join([ _ for _ in Ck[j]])
					if key not in L2.keys():
						L2[key] = 0
					L2[key] += 1
		# 剔除小于min_sup的项集
		temp = []
		for i in L2.items():
			if i[1] < min_sup:
				temp.append(i[0])
		for i in temp:
			del L2[i]
		# 将新找出的频繁项集加入保存频繁项集的变量Lk
		l = []
		for i in L2.items():
			ll = []
			for j in range(0, len(i[0]), 2):
				ll.append(i[0][j:j+2])
			l.append(ll)
		Lk.append(l)
		del l
		k += 1
	
	# 输出找到的频繁项集
	for i in range(len(Lk)):
		print(Lk[i])
