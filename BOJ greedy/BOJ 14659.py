T = int(input())
Peak = list(map(int, input().split(" ")))
cnt = 0
answer = 0
result=0
state = Peak[0]
for i in range(1, len(Peak)):
    if (state > Peak[i]):  # 현재값이 오른쪽값보다 크면서, 다음 봉우리가 있을때
        cnt += 1

    else: # 현재 봉우리보다 다음 봉우리가 높을때
        state = Peak[i]  # 이전 봉우리보다 높은 봉우리로 기준 갱신
        if (answer < cnt):  # 여태 최고 처치수보다 클때 최고 처치수 갱신
            answer = cnt
        cnt = 0
    result=max(answer,cnt)#이전 최고 처치수와 마지막 처치수 비교


print(result)
