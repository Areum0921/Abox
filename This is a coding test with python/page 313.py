
S=input()

answer1=0 # 1의 덩어리 개수
answer2=0 # 0의 덩어리 개수

# 덩어리 별로 뒤집는것 -> 덩어리 개수가 작은 수를 뒤집어야 더 적은 횟수로 같은 숫자 만들기 가능
if S[0]=='1':
    check=False
elif S[0]=='0':
    check=True

for i in S:
    if i=='1' and check==False: # 1 덩어리 첫부분 발견됐을때
        check=True
        answer1 += 1
    elif i=='0' and check==True: # 처음이거나, 1덩어리가 끝나고 0이 발견됐을때
        check=False
        answer2 +=1


print(min(answer1,answer2))
