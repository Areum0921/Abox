N, L = map(int,input().split(" "))#물이 새는곳 개수, 테이프 길이
loc=list(map(int, input().split(" "))) #물이 새는곳 위치
#테이프길이가 2, 새는곳이 1,2라면 테이프는 0.5~2.5에 부착해서 막는다
loc.sort()
tape=[]
sum=0 #필요 테이프 개수
use=L-1#현재 테이프의 남은길이(양옆 0.5로 인해 길이 1은 제외)
for i in range(N-1,-1,-1):
    print(loc[i], loc[i - 1], use, tape)
    if(i==0):
        sum+=1
    if (loc[i] - loc[i - 1]<=L-1 and use-(loc[i] - loc[i - 1])>=0):
        # 다음 구멍까지 길이가 현재 사용중인 테이프길이보다 짧다면 현재 사용중인 테이프사용
        use -=loc[i]-loc[i-1]
    else:#새테이프가 필요할때
        print("새테이프로바꾸기")
        sum+=1 #테이프개수 1증가
        use = L - 1


print(sum)