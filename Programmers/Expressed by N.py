# 각 숫자를 n번 사용하는 경우 만들 수 있는 수들을 더해 나가면된다.
# N=5일때
# dp[1] = {5}
# dp[2] = {5*5, 5+5, 5-5, 5/5}
# dp[3] = {dp[1] 사칙연산 4가지 dp[2], dp[2] 사칙연산 4가지 dp[1]} , 순서에따라 결과값도 달라지기때문

def solution(N, find):
    answer = -1
    dp =[]
    for i in range(1, 9): # 최대 8개까지 (최소값이 8보다 크면 -1)
        number = { int(str(N) * i) } # 중복 제거용 set
        for j in range(0,i-1): # N이 4개인경우 1,3 / 2,2 / 3,1
            # 4개일때의 경우 dp[0~2] (인덱스 기준 dp[n]에는 n+1개의 숫자를 사용한 경우다.)
            for k in dp[j]: # dp[0,1,2], -1 = 2, -2= 1, -3 = 0
                for w in dp[ -j - 1]: # dp[0],dp[-1]= dp[0],dp[2], dp[1],dp[-2] = dp[1],dp[1], dp[2],dp[-3] = dp[2],dp[0]
                    number.add(k + w)
                    number.add(k - w)
                    number.add(k * w)
                    if w != 0:
                        number.add(k // w)

            if find in number:
                print(i)
                return i
        dp.append(number)
    print(dp)
    return answer


N=5
find=12
solution(N,find)