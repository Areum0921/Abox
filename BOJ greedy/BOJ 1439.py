import sys
S=sys.stdin.readline()

cnt0=0 # 0이 연속되는 덩어리 개수
cnt1=0 # 1이 연속되는 덩어리 개수

for i in range(1,len(S)):
    if(S[i]=='0' and S[i-1]=='1'):
        cnt1+=1
    elif(S[i]=='1' and S[i-1]=='0'):
        cnt0+=1
    elif(i==len(S)-1):
        if(S[i-1]=='1'):
            cnt1+=1
        elif(S[i-1]=='0'):
            cnt0+=1

print(min(cnt0,cnt1))

#수행시간 빠르게 하는법 S.split(str(0))을 하면
#100001001100 이 1, "", 1, "" ,11,"" 이된다.



