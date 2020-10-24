f = open('./test1.txt', 'w')
for i in range(1, 10001):
    f.write(str(i)+'\n')
f.close()
