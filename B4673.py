n = set(range(1, 10001)) #1부터 10000까지 
g = set()#비어있음

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    g.add(i) # 셀프넘버가 아닌것들

sn= n - g # 전체에서 셀프넘버가 아닌것들을 뺌.

for i in sorted(sn): #정렬
    print(i)
