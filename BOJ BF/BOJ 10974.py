N=int(input())
check=[False]*N # 중복사용방지
result=[]

def solution():
    if(len(result)==N):
        print(' '.join(list(map(str, result))))

    for i in range(N):
        if(check[i]==False): # 사용되지않은 숫자일때
            check[i]=True # 사용여부 체크
            result.append(i+1)
            solution()
            check[i]=False
            result.pop()

solution()