import time
from time import time as the_timer
import datetime
import time
import numpy as np
import random

word_list=	[[0,'meager','缺乏',2,1], [1,'meddlesome','好干涉的',2,1], [2,'medley','混合',2,1],[3,'menagerie','一群',2,1],[4,'meticulous','小心的',2,1],[5,'mettle','勇气',2,1],
			[6, 'menial', '下贱的',2,1], [7, 'milieu','环境',2,1], [8, 'mire', '陷入泥潭', 2,1], [9,'miserly', '贪婪吝啬', 2,1]]

length = len(word_list) -1
test_size=[0,0,0,0,0,0]

def init():
	for a in range(0, length):
		word_list[a][3]	= random.randint(1,8)
		word_list[a][4] = random.randint(1,3)

def word_test(index):
	print(str(word_list[index][1])) #只看得到看单词
	t1 = the_timer()
	evalu1 = input()
	if evalu1 == 'y': #knowthemeaning
		t2 = the_timer()
		delta = t2 - t1
		print('compare' + str(word_list[index][1]) + str(word_list[index][2]))
		evalu2 = input()
		if evalu2 == 'y':
			word_list[index][3] += int(delta/0.9)
			print('T')
		else:
			word_list[index][3] = 7
			print('F' + ' ' + str(word_list[index][1]) + '  ' + str(word_list[index][2]))
	else:
		word_list[index][3] = 4
		print('F' + ' ' +  str(word_list[index][1]) + '  ' + str(word_list[index][2]))


def size():
	choose_size = 0
	for i in range(0, length):
		dif = word_list[i][3]
		z = 1 + np.exp(2*np.log(3) - dif + 1)
		freq = int(10/z)
		choose_size += freq
		word_list[i][4] = freq
	return choose_size

def run_today(amt):
  ##概率函数决定word_list[index]中index的值
  ##每天选择choose_size个单词
	j = 0
	temp = 0
  
	for n in range(1,99):	
		for j in range(0, length):
			rand = random.random()
			rim = word_list[j][4]/amt
			if rand <= rim: ##选中
				word_test(j)
				

				if temp == amt:
					print('The end')
				else:
					temp += 1

				show_progress(temp)
		
		if temp == amt:
			print('The end')
			break	

def show_progress(temper):
	left = test_size[s] - temper
	print('the size is:' + str(test_size[s]))
	print('the remianing is:' + str(left))



for s in range(0, len(test_size) - 1):

	test_size[s] = size()
	run_today(test_size[s])
	print(word_list)
	print('this is the end of ' + str(s + 1) + 'nd' + ' ' + 'round')
