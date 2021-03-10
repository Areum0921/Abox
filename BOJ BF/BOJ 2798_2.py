# 3중 for문으로 구현하기
# 336ms -> 112ms
N, M =map(int,input().split(" "))
card_deck=list(map(int,input().split(" ")))
max_sum=0
card_sum=0

for i in range(len(card_deck)-2):# 첫번째 카드뽑을때 최소 2개의 카드는 남아있어야함
    for j in range(i+1,len(card_deck)-1): # 마찬가지로 2번째 카드뽑을때 최소1개의 카드는 남아야함
        for k in range(j+1,len(card_deck)): # 마지막카드뽑을때는 안남아도 됨
            card_sum=card_deck[i]+card_deck[j]+card_deck[k]
            #print(card_deck[i],card_deck[j],card_deck[k])
            if(card_sum>=max_sum and card_sum<=M):
                max_sum=card_sum

print(max_sum)

