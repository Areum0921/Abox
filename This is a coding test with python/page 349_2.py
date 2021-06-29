# permutations을 사용하지 않고 dfs를 이용하면 시간 훨씬 단축
N = int(input())
number = list(map(int, input().split(" ")))
add, sub, mul, div = map(int,input().split(" "))

min_value = 99999999
max_value = -99999999

def dfs(i, now):
    global min_value, max_value, add, sub, mul, div

    if i==N: # 모든 수에 대해서 연산 했으면
        min_value=min(min_value, now)
        max_value=max(max_value, now)

    else:
        if add > 0:
            add -= 1
            dfs(i+1,now+number[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1,now-number[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1,now*number[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1,int(now / number[i]))
            div += 1

dfs(1,number[0]) # i는 숫자 개수 1개부터 N개까지

print(max_value)
print(min_value)






