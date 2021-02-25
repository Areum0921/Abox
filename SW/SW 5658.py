def find_num(slist):
    while(1):# 돌렸을때 처음이랑 같을때까지 반복
        str=""
        for i in range(N):#N//4개(각변의 숫자 개수)마다 잘라서 16진수 만들어주기
            str+=slist[i]
            if(len(str)==N//4):
                if(int(str, 16) not in sum_list): #해당값이 이미 있는지
                    sum_list.append(int(str, 16))
                str =""


        slist.append(slist.pop(0))
        if(slist==rotate):
            break

    sum_list.sort(reverse=True)#내림차순
    return sum_list[K-1] #K번째 큰숫자 (인덱스는 0부터니까 K-1)

T=int(input())

for i in range(T):
    N, K=map(int,input().split(" ")) #N개의 숫자, K번째 큰수
    slist=input()
    slist=list(slist)

    rotate=slist[:] #slist가 변경되어도 초기값 상태를 가지고있음
    sum_list=[]
    print("#%d" %(i+1),find_num(slist))







