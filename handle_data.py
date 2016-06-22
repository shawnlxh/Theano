# -*- coding: utf-8 -*-
import gzip
import cPickle as p
import numpy
import random

f = open('desktop/训练数据.txt')
list = []       # get the training data，and remove the ENTER in the end of the line.
for i in f:
    list.append(i[0:-1])

for i in range(1000):
    list[i] = list[i].split('\t')

list_data = []     # sunder the labels from the data
for i in range(1000):
    line = list[i][1]+list[i][2]+list[i][3]+list[i][4]
    list_data.append(line)
    
list_label = []
for i in range(1000):
    line = list[i][0]
    list_label.append(line)
   
list2 = []    #transform the training data to the apropriate format
train_data = []
for i in range(900):
    for j in range(21):
        list2.append(list_data[i][j])
    train_data.append(list2)
    list2 = []
    
train_data = numpy.array(train_data,dtype = float)
train_data = train_data/10
    
list2 = []
train_label = []
for i in range(900):
    list2.append(list_label[i])
    train_label.append(list2)
    list2 = []

train_label1 = []
for i in range(900):
    if train_label[i][0] != '0' and train_label[i][0] != '1':
        train_label[i][0] = '1' 
    
    train_label1.append(train_label[i][0])

train_label = numpy.array(train_label1, dtype = int)

train_set = train_data, train_label

valid_data = []    #得到CV数据和标签的合适格式
list2 = []
i = 900
while i < 1000:
    for j in range(21):
        list2.append(list_data[i][j])
    valid_data.append(list2)
    list2 = []
    i = i+1
    
valid_data = numpy.array(valid_data,dtype = float)
valid_data = valid_data/10

valid_label = []
list2 = []
i = 900
while i < 1000:
    list2.append(list_label[i])
    valid_label.append(list2)
    list2 = []
    i = i+1
    
valid_label1 = []
for i in range(100):
    if valid_label[i][0] != '0' and valid_label[i][0] != '1':
        valid_label[i][0] = '1' 
    
    valid_label1.append(valid_label[i][0])

valid_label = numpy.array(valid_label1, dtype = int)

valid_set = valid_data, valid_label

        
f = open('desktop/测试数据.txt')
list = []
for i in f:
    list.append(i[0:-1])

for i in range(200):
    list[i] = list[i].split('\t')

list_data = []    
for i in range(200):
    line = list[i][1]+list[i][2]+list[i][3]+list[i][4]
    list_data.append(line)
    
list_label = []
for i in range(200):
    line = list[i][0]
    list_label.append(line)
    
list2 = []
test_data = []       #得到测试数据和标签的合适格式
for i in range(200):
    for j in range(21):
        list2.append(list_data[i][j])
    test_data.append(list2)
    list2 = []
    
test_data = numpy.array(test_data,dtype = float)
test_data = test_data/10   
    
list2 = []
test_label = []
for i in range(200):
    list2.append(list_label[i])
    test_label.append(list2)
    list2 = []
    
test_label1 = []
for i in range(200):
    if test_label[i][0] != '0' and test_label[i][0] != '1':
        test_label[i][0] = '1' 
        
    test_label1.append(test_label[i][0])

test_label = numpy.array(test_label1,dtype = int)

test_set = test_data, test_label

output = open('desktop/data.pkl','wb')    #用cPickle将其序列化
p.dump(train_set, output)
p.dump(valid_set, output)
p.dump(test_set, output)

output.close()

f = gzip.open('desktop/data.pkl.gz','wb')  #压缩数据
f2 = open('desktop/data.pkl','rb')
f.writelines(f2)
f.close()
f2.close()
