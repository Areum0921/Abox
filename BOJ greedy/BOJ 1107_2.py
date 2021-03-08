# 시간을 줄일방법 생각하기
# N을 기준으로 N에서 -1씩빼면서 만들수있는 N이하 수 중 제일 높은수(dstr),
# 마찬가지로 +1씩하면서 N이상 수 중 제일 낮은수(ustr),
# dstr ,ustr, 100(처음시작채널)을 각각 기준으로 필요한 버튼횟수 중 최소값 구해주기
# 3108ms -> 312ms ~!
button=[0,1,2,3,4,5,6,7,8,9]
start=100 # 시작 채널

N=str(input())
M=int(input())
#M이 0이고 3번째줄에 아무 입력이 없을때 예외처리를 해주지 않아 런타임오류
if(M!=0): # 고장난 버튼이 있을경우 3번째줄 입력.
    broken = list(map(int, input().split(" ")))
for i in range(M): # 고장난 버튼 제외시키기
    del button[button.index(broken[i])]


first=abs(start-int(N))# 현재채널 100번에서 +,-로 이동하는경우

down=int(N)
up=int(N)
second=999999
third=999999
if(len(button)>0):#누를수 있는 버튼이 있을때
    while(1): # N이하 숫자중 만들수있는 가장 가까운 숫자
        dstr=""
        cnt=0
        for i in range(len(str(down))):

            if(int(str(down)[i]) not in button):
                cnt+=1
                break
            else:
                dstr+=str(down)[i]
        if(cnt==0 or down==0): # 더이상 내릴 숫자가 없을때도 종료처리
            break
        if(down>0):
            down-=1


    while(up<1000001): # N이상 숫자중 만들수있는 가장 가까운 숫자
        ustr=""
        cnt=0
        for i in range(len(str(up))):
            if(int(str(up)[i]) not in button):
                cnt+=1
                break
            else:
                ustr+=str(up)[i]
        if(cnt==0):
            break
        up+=1
    if(len(dstr)>0):
        second = abs(int(dstr) - int(N)) + len(dstr)  # 가장가까운 낮은숫자기준으로 버튼횟수
    if(len(ustr)>0):
        third = abs(int(ustr) - int(N)) + len(ustr)  # 가장가까운 높은숫자기준으로 버튼횟수

answer=min(first,second,third)#가장 낮은 횟수
print(answer)








