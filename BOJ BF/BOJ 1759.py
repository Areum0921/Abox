# 완전탐색할경우, 시간초과로 실패함. 탐색할 부분을 줄여주는게 관건
# 오름차순 구성이므로, 현재 password 위치가 c라면 a,b는 비교 안해도 된다는 점을 이용.
import time
start=time.time()
N, M = map(int, input().split(" "))
alphabet=list(map(str, input().split(" ")))

check=[True]*M
alphabet.sort()
make=[]

def password(index,N, M):
    if (len(make)==N):
        cnt_V=0 # 모음
        cnt_C=0 # 자음
        for i in make: # 자음, 모음 개수 카운트
            if (i in 'aeiou'):
                cnt_V+=1
            else:
                cnt_C+=1
        if (cnt_V>0 and cnt_C>1): # 모음이 1개이상, 자음이 2개이상인경우 출력
            print(''.join(map(str, make)))
        return

    for i in range(M):
        if(check[i]==True and i>=index): # 오름차순 구성이므로 현재 i위치 이후 알파벳만 비교
            check[i]=False
            make.append(alphabet[i])
            password(i, N, M)
            check[i]=True
            make.pop()

password(0,N, M)
print(time.time()-start)

