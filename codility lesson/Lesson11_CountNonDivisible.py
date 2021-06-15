# 자신을 나눌 수 없는 요소 개수
def solution(A):

    N = len(A)
    count=[0]*(N*2+1) # 최대값은 N*2, 각각의 수가 몇번씩 나왔는지
    result=[0]*N
    check=[-1]*(2*N+1)

    for num in A:
        count[num]+=1 # 해당 숫자 빈도수

    for i in range(N):
        cur = A[i] # 현재 숫자

        if check[cur] != -1: # cur에 대해 이미 계산한적 있으면
            result[i] = check[cur]

        else:
            cnt=0
            for j in range(1, int(cur ** 0.5)+1): # 현재 숫자의 제곱근까지만
                # 12의경우 나뉘는 수는 1,2,3,4,6,12.
                # 12 ** 0.5는 3.4xx
                # 4까지 구해준다. 그럼 1을 구하면 12
                # 2를 구하면 6
                # 3을구하면 4라는 값도 얻을 수 있기 때문.
                if cur % j == 0: # A[i]가 j로 나뉘는경우
                    print(cur,j)
                    cnt += count[j] # j의 빈도수 만큼 카운팅

                    if j != cur // j: # j * j = cur가 아닌경우
                        cnt += count[cur//j] # j * cur//j = cur
                        # cur = 12면 j=3일때 3 * 12//3 = 12
                        # 1개의 j를 구하면 다른 i도 구할 수 있음.

            print(count,A[i],N,cnt)
            # cnt 개수는 해당 숫자를 나눌 수 있는 숫자 수
            result[i] = N - cnt # i를 나눌 수 없는 수는 전체 개수 - cnt 개수
            check[cur] = result[i]

    return result



A=[3,1,2,3,6]
solution(A)