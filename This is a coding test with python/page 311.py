# 공포도가 높을수록 사람많이필요
# 그룹수가 많아야 하니, 적은 인원수를 필요로 하는 그룹부터 구성해나간다.
N=input()
fear = list(map(int,input().split()))
fear.sort()
answer=0
cnt=0

for i in fear:
    cnt+=1
    if cnt>=i: # 현재 누적 인원수가 공포도 보다 높으면 그룹 가능
        answer+=1
        cnt=0

print(answer)
