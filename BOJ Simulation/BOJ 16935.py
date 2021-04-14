# 구현 해야할 부분이 많음... 시간이 오래걸림
# 매 func마다 answer를 선언 하니까 결과 이상하게 나오는거 멈춤.
# 구현 문제에서 시간을 많이 쓰게된다니까 충분한 연습이 필요하다.
import sys
input = sys.stdin.readline
N,M,R=map(int,input().split(" "))
array=[list(map(int,input().split(" "))) for _ in range(N)]
func=input().split(" ")
answer=[[]*M for _ in range(N)]

def func1(): # 1번 연산 상하 반전
    global array
    array=array[::-1]

def func2(): # 2번 연산 좌우 반전
    global array
    for i in range(N):
        array[i]=array[i][::-1]




def func3(): # 3번 연산 오른쪽방향 90도 회전
    global N,M,array
    N,M = M,N
    answer=[[]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            answer[i].append(array[M-j-1][i])
    array=answer

def func4(): # 4번 연산 왼쪽방향 90도 회전
    global N,M,array
    N,M = M,N
    answer=[[]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            answer[i].append(array[j][N-i-1])
    array=answer


def func5(): # 5번 연산
    global array
    answer = [[0] * M for _ in range(N)]
    for i in range(2):
        for j in range(N//2):
            answer[i*(N//2)+j]=array[N//2+j][M//2*i:M//2*(i+1)]+\
                               array[j][M//2*i:M//2*(i+1)]
    array=answer


def func6(): # 6번 연산 ( 5번과 반대방향
    global array
    answer=[[0]*M for _ in range(N)]
    for i in range(2):
        for j in range(N//2):
#            print(i*(N//2)+j)
#            print(array[j][M-((M//2)*(i+1)) : M-((M//2)*i)]+array[j+N//2][M-((M//2)*(i+1)) : M-((M//2)*i)])
            answer[(i*(N//2))+j]=array[j][M-((M//2)*(i+1)) : M-((M//2)*i)]+array[j+N//2][M-((M//2)*(i+1)) : M-((M//2)*i)]
    array=answer
    #print("arraY",array)
    #print("answer",array)

for k in func:
    if(int(k)==1):
        func1()
    elif(int(k)==2):
        func2()
    elif(int(k)==3):
        func3()
    elif(int(k)==4):
        func4()
    elif(int(k)==5):
        func5()
    elif(int(k)==6):
        func6()

for j in range(len(array)):
    print(' '.join(map(str, array[j])))


