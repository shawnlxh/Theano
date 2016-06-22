f = open('desktop/userid_profile.txt')
list = []
for i in range(23669283):
    line = f.readline()
    list.append(line)
    
j = 1
k = 1
n = 1
for i in range(30000000):  //这里会提示超出list的长度了，我的处理是将内存里的list输出到一个.txt里
    if (i+1) == (n * 10):
        k = k + 1
        n = n * 10
    if int(list[i][0:k]) != j:
        print i
        print int(list[i][0])
        list.insert(j-1,'0\t0\t0\n')
    j = j+1
