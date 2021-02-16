N=int(input())
w=[]
max_w=0
for i in range(N):
    w.append(int(input()))#각 로프들이 버틸수 있는무게
w.sort()#버틸수있는 무게를 작은 순으로 나열

for i in range(N):
    if(max_w<w[i]*(N-i)): # 제일큰값 찾기
        max_w=w[i]*(N-i)
    #제일 작은거 무게 * 로프개수
    #그 다음 작은거 무게 * 로프개수(이전 로프 제외)
#ex) 10 30 40 일경우
# 10 30 40 사용시 10x3 = 30
# 30 40 사용시 30x2 = 60
# 40 사용시 40x1 = 40

print(max_w)