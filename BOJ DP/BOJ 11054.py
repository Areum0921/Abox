# 증가하는 수열, 감소하는 수열들을 구하고 합쳐본다
# ex) A=1 2 1 5 2 1 일때
# 증가하는 수열은 dpu=[1,2,1,3,2,1] / 1, 1,2, 1, 1,2,5, 1,2, 1
# 감소하는 수열은 dpd=[1,2,1,3,2,1] / 1, 2,1, 1, 5,2,1, 2,1, 1
# 제일 긴 바이토닉은 dpu[i]+dpd[i+1]의 최대값임
# i가 0일때 dpu[0] = 1 dpd[1]=2 -->1, 2,1  == 3
# i가 1일때 dpu[1] = 2 dpd[2]=1 -->1, 2,1  == 3
# i가 2일때 dpu[2] = 1 dpd[3]=3 --> 1, 5,2,1 == 4
# i가 3일때 dpu[3] = 3 dpd[4]=2 --> 1,2,5, 2,1 == 5
# i가 4일때 dpu[4] = 2 dpd[5]=1 --> 1,2 , 1 == 3
# 이중 최대값이 가장 긴 바이토닉 부분 수열.

N=int(input())
A=list(map(int, input().split(" ")))
#print(A)
dpu=[1]*N
dpu[0]=1
dpd=[1]*N
dpd[0]=1

def longA(a,u): # 증가수열
    for i in range(1,N):
        for j in range(i):
            if(a[j]<a[i] and u[i]<u[j]+1):
                u[i]=u[i]+1

def shortA(a,d): # 감소수열 (뒤에서부터 증가하는 형태)
    for i in range(N-1,-1,-1):
        for j in range(N-1,i,-1):
            if (a[i] > a[j] and dpd[i] < dpd[j] + 1):
                dpd[i] = dpd[i] + 1

longA(A,dpu)
shortA(A,dpd)
maxA=1
if(len(A)>1):
    for i in range(N-1):
        #print(dpu[i])
        if(maxA<dpu[i]+dpd[i]-1): # 0~i까지의 증가수열길이 + i~N까지의 증가수열길이 -1 (-1은 i의 길이 1이 2번더해짐)
            maxA = dpu[i] + dpd[i] - 1
"""
if(A[i]==A[i+1]): # 이렇게하면 틀림 
    maxA=dpu[i]+dpd[i+1]-1
else:
    maxA=dpu[i]+dpd[i+1]
"""



#print(dpu)
#print(dpd)
print(maxA)
