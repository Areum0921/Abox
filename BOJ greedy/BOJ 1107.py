# 시간을 줄일방법 생각하기
button=[0,1,2,3,4,5,6,7,8,9]
start=100 # 시작 채널

N=str(input())
M=int(input())
#M이 0이고 3번째줄에 아무 입력이 없을때 예외처리를 해주지 않아 런타임오류
if(M!=0): # 고장난 버튼이 있을경우 3번째줄 입력.
    broken = list(map(int, input().split(" ")))
for i in range(M): # 고장난 버튼 제외시키기
    del button[button.index(broken[i])]


cnt=abs(start-int(N))# 현재채널 100번에서 +,-로 이동하는경우

for i in range(0,1000001):
    #500,000보다 윗번호에서 - 해서 내려오는 경우도 있으므로
    str1=""
    #print("몇자리수",i,len(str(i)))
    for j in range(len(str(i))):
        if (int(str(i)[j]) not in button):
            break
        else:
            str1 += str(i)[j]
        #print("조합한숫자",str1)
        #print("버튼 누르는 횟수",abs(int(N) - int(str1))+len(str1))
        if(abs(int(N) - int(str1))+len(str1)<cnt):

            cnt=abs(int(N) - int(str1))+len(str1)


print(cnt)







