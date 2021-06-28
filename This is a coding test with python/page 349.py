from itertools import permutations
N = int(input())
number = list(map(str, input().split(" ")))
op = list(map(str, input().split(" ")))
min_value = 99999999
max_value = -99999999
op_list=[]
for i in range(len(op)):
    for j in range(int(op[i])):
        if i==0:
            op_list.append('+')
        elif i==1:
            op_list.append('-')
        elif i==2:
            op_list.append('*')
        else:
            op_list.append('//')

for j in list(permutations(op_list,len(op_list))):
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






