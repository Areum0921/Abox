def solution(food):
    dp=[0]*len(food)
    dp[0]=food[0]
    dp[1]=max(food[0],food[1])
    for i in range(2,len(food)):
        dp[i]=max(dp[i-2]+food[i],dp[i-1]) # 현재 식량칸을 털지 안털지
        # 전전 식량창고까지 턴 최대식량 + 현재 식량 과 이전창고까지 턴 식량의 최대값 중 큰값 선택.
    print(dp)

food=[1,3,8,5]

solution(food)



