# 연속된 숫자들의 합이 n
def solution(n):
    answer = 1 # 맨마지막 숫자 자신
    for i in range(1,n+1):
        ans=[]
        ans.append(i)
        num=i
        for j in range(i+1,n+1):
            num+=j
            ans.append(j)
            if(num==n): # i부터 연속된 수의 합이 n인경우를 발견했을때, 더이상 계산할 필요 x
                print(ans)
                answer+=1
                break
            if(num>n): # i부터 연속된 수의 합이 초과시에 더이상 계산할 필요 x
                break
    print(answer)
    return answer


n=10
solution(n)