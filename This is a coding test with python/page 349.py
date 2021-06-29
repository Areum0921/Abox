# 시간 초과
# permutations를 사용할때 set을 이용해주면 통과하나 시간이 오래걸림

from itertools import permutations
N = int(input())
number = list(map(str, input().split(" ")))
add, sub, mul, div = map(int,input().split(" "))
sum_op = add + sub + mul + div
min_value = 99999999
max_value = -99999999
op_list=[]
for i in range(sum_op):
    if add>0:
        add-=1
        op_list.append('+')
    elif sub>0:
        sub-=1
        op_list.append('-')
    elif mul>0:
        mul-=1
        op_list.append('*')
    elif div>0:
        div-=1
        op_list.append('//')

for j in set(permutations(op_list,len(op_list))): # set으로 중복 제거
    temp = number[0]
    for k in range(1,len(number)):
        if j[k-1]=='//' and int(temp)<0: # 음수 나눌때 양수로 바꾼후 몫을 다시 음수로 전환
            temp = str(int(temp)*-1)
            temp = str(eval(temp + j[k - 1] + number[k]))
            temp = str(int(temp)*-1)
        else:
            temp = str(eval(temp + j[k - 1] + number[k]))

    min_value = min(min_value, int(temp))
    max_value = max(max_value, int(temp))

print(max_value)
print(min_value)






