# -*- coding: utf-8 -*-
import linecache
list1 = [] #存储原始训练数据
f = open("desktop/data.txt")
for i in f:
	list1.append(i)
	
for i in range(1000):  #存储分割后的训练数据
	list1[i] = list1[i].split("	")
	
for i in range(1000):  #存储所需元素
	list1[i] = list1[i][0]+"	"+list1[i][6]+"	"+list1[i][11]

list2 = []  #分割所需元素
for i in range(1000):
	line = list1[i].split("	")
	list2.append(line)

for i in range(999):  #取出末尾的\n
	list2[i][2] = list2[i][2][0:-1]

list3 = []
for i in range(1000):  #存储所需的用户数据
	line = linecache.getline('desktop/user_data.txt', int(list2[i][2]))
	line = line.split('\t')
	list3.append(line)
			
for i in range(1000):  #取出末尾的\n
	list1[i] = list1[i][0:-1]

for i in range(1000):  #过渡数据0\t3\t490234\t1\t3\n
	list1[i] = list1[i]+"	"+list3[i][1]+'\t'+list3[i][2]	
list3 = []
		
for i in range(1000):  #取出末尾的\n
	list1[i] = list1[i][0:-1]
 
for i in range(1000):  #分割过渡数据
	list1[i] = list1[i].split("	")


for i in range(1000):  #取出(sex,age)元组
	list2[i] = (list1[i][3],list1[i][4])
	
d = {('0','1'): '100000000000000000'}
d[('0','2')] = '010000000000000000'
d[('0','3')] = '001000000000000000'
d[('0','4')] = '000100000000000000'
d[('0','5')] = '000010000000000000'
d[('0','6')] = '000001000000000000'
d[('1','1')] = '000000100000000000'
d[('1','2')] = '000000010000000000'
d[('1','3')] = '000000001000000000'
d[('1','4')] = '000000000100000000'
d[('1','5')] = '000000000010000000'
d[('1','6')] = '000000000001000000'
d[('2','1')] = '000000000000100000'
d[('2','2')] = '000000000000010000'
d[('2','3')] = '000000000000001000'
d[('2','4')] = '000000000000000100'
d[('2','5')] = '000000000000000010'
d[('2','6')] = '000000000000000001'

answer = []
for i in range(1000):
    line = list1[i][0]+'\t'+list1[i][1]+'\t'+list1[i][3]+'\t'+list1[i][4]
    answer.append(line)
    answer.append('\t')
    line = d[list2[i]]
    answer.append(line)
    answer.append('\n')
    
f5 = open("desktop/5.txt",'w')
for i in range(4000):
    f5.writelines(answer[i])
f5.close()
