# BF로 구현, 하지만 카드개수가 100개까지고, 카드 3개만 뽑으면되서 3중 for문이 시간 더짧을듯..
# 336ms
N, M = map(int,input().split(" "))
card_deck=list(map(int,input().split(" ")))
check=[False]*N
num=[]
sumlist=[]
def finding(M):
    if(len(num)==3): # 3개의 숫자를 골랐을때
        if(sum(num)<=M): # 3개 숫자합이 M보다 낮을때 sumlist에 추가
            sumlist.append(sum(num))
        return

    for i in range(len(check)):
        if(check[i]==False): # 사용하지 않았던 카드일때
            check[i]=True # 사용여부 체크
            num.append(card_deck[i]) # 리스트에 추가
            finding(M)
            #print(num)
            check[i]=False
            num.pop() #

finding(M)
print(max(sumlist))


