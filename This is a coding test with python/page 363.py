import heapq
# 정렬 후 카드 개수가 적은 묶음부터 비교시작
# 힙은 최대값이나 최소값을 필요로 할 경우 사용
N=int(input())
deck = []
for i in range(N):
    card = int(input())
    heapq.heappush(deck, card)

answer = 0

while len(deck)!=1:
    deck1=heapq.heappop(deck) # 최소값 꺼내기
    deck2=heapq.heappop(deck) # 최소값 꺼내기
    answer += deck1+deck2
    heapq.heappush(deck,deck1+deck2)

print(answer)