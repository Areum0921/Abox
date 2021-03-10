N,M=map(int,input().split(" "))
check=[False]*N
num_list=[]
def finding(N,M):
    if(len(num_list)==M):
        print(' '.join(map(str, num_list))) # ' '로 구분하여 숫자 리스트들을 한줄로 출력
        return # return을 넣어주지않으면 num_list길이 N까지 모두 탐색해버림

    for i in range(N):
        if(check[i]!=True): # 방문하지 않았다면
            check[i]=True # 방문하고, 방문했음을 체크
            num_list.append(i+1)
            #print(num_list)
            #print(check)
            finding(N,M)
            check[i]=False # 더 이상 방문할곳이 없으면, 이전상태로 되돌리기
            num_list.pop() # 방문한지 가장 오래된곳 없애기

finding(N,M)