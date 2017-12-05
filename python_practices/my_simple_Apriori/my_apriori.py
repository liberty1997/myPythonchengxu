#!/bin/python3

import pandas as pd

def load_data(f, sep = ' '):
	return pd.DataFrame(pd.read_csv(f, header = None, sep = sep))

def find_frequent_1_itemsets(D):
	C1 = {}
	L1 = {}
	items = []
	for i in range(len(D)):
		item = D[i].split(',')
		for it in item:
			if it not in C1.keys():
				C1[it] = 0
			C1[it] += 1
			if it not in items:
				items.append(it)
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
	Ck = []
	print('[apriori_gen] K, Lk_1', K, Lk_1)
	if len(Lk_1[0]) < 2:
		# 求2频繁项集候选集
		print('----IF----')
		for i in range(len(Lk_1) - 1):
			for j in range(i+1, len(Lk_1)):
					c = []
					c.append(Lk_1[i][0])
					c.append(Lk_1[j][0])
					c.sort()
					Ck.append(c)
					del c
		#print('11111', Ck)
		#return Ck
	else:
		# 求3频繁项集候选集及以上
		print('----ELSE----')
		print('Lk_1=', Lk_1)
		print(str(K) + '项集候选集')
		for i in range(len(Lk_1) - 1):
			for j in range(i + 1, len(Lk_1)):
				c = []
				a = 0
				for ii in range(len(Lk_1[0]) - 1):
					if Lk_1[i][ii] != Lk_1[j][ii]:
						a = 1
				if a == 0 and Lk_1[i][len(Lk_1[0]) - 1] < Lk_1[j][len(Lk_1[0]) - 1]:
					for t in range(len(Lk_1[0])):
						c.append(Lk_1[i][t])
					c.append(Lk_1[j][len(Lk_1[0]) - 1])
					print('c=', c)
					c = list(set(c))
					c.sort()
					print('Sorted c=',c)
					# 进行剪枝 求子集
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
					if a == 0:
						Ck.append(c)
					#print('Ck=', Ck)
				del c
	if len(Ck) == 0:
		return None
	else:
		print(str(len(Lk_1[0]) + 1) + '项集最终候选集 Ck=', Ck)
		return Ck



# 最小支持度
min_sup = 2
data = load_data('apriori_data.csv', sep = ' ')
itemsets = []
for i in range(len(data[1])):
	ii = data[1][i].split(',')
	itemsets.append(ii)
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
	Ck = apriori_gen(k, Lk[k - 2])
	print('k = ',k)
	print('传入的Lk-1=', Lk[k - 2])
	if Ck == None:
		break
	L2 = {}
	for j in range(len(Ck)):
		for i in range(len(itemsets)):
			if set(Ck[j]).issubset(set(itemsets[i])):
				key = ''.join([ _ for _ in Ck[j]])
				if key not in L2.keys():
					L2[key] = 0
				L2[key] += 1
	temp = []
	for i in L2.items():
		if i[1] < min_sup:
			temp.append(i[0])
	for i in temp:
		del L2[i]
	l = []
	for i in L2.items():
		ll = []
		for j in range(0, len(i[0]), 2):
			ll.append(i[0][j:j+2])
		l.append(ll)
	Lk.append(l)
	del l
	k += 1
	#Lk.append([])
	#print(Lk)
print(Lk)
