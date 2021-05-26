# 더 간단하게 제일 큰수를 몇번 더하는지 알면 된다.
# 전체 더하는 수 = 제일 큰수 더하는 횟수 + 그 다음 수 더하는 횟수
# 제일 큰수 더하는 횟수 m//k * k
# m이 8이고 k가 3이면 제일큰수는 8//3 * k == 2 * 3 == 6번

def solution(n,m,k):
    answer=0
    n=sorted(n,reverse=True)
    cnt_1=m//k * k # 첫번째 수
    cnt_2=m-cnt_1 # 두번째 수

    answer = n[0]*cnt_1 + n[1]*cnt_2

    print(answer)
    return answer

n=[2,4,5,4,6]
m=8
k=3
solution(n,m,k)