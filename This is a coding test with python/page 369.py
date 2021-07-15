# 와이파이는 집에만 설치 가능

N,C = map(int,input().split(" "))

house_loc=[]
for i in range(N):
    house_loc.append(int(input()))


house_loc.sort() # 이진탐색은 반드시 정렬 해야함.

# 최소간격 ~ 최대간격 사이로 범위를 주고 중간간격부터 설치해보며 간격을 조절하며 찾는다.
start=1 # 최소 간격
end=house_loc[-1]-house_loc[0] # 첫집~마지막집 사이 거리 (최대간격)
#print(start,end)
answer = 0

while (start <= end):
    mid = (start+end)//2  # 가운데

    value = house_loc[0] # 첫집에 공유기 설치 하고 시작
    # 공유기끼리의 최소 길이를 최대로 해야하니
    # 첫 집부터 각 간격마다 설치해보고 가능한 경우 중 가장 큰 간격을 도출한다.
    cnt=1

    for i in range(1,N):
        if house_loc[i] >= value + mid: # 이전에 설치된 공유기 위치 + 간격 보다 큰 좌표의 다음 집에 설치
            value=house_loc[i] # 이전에 설치된 공유기 위치 갱신
            cnt+=1 # 공유기 개수 올리기

    if cnt>=C: # 설치된 공유기 수가 C이상이면
        start = mid+1 # 간격을 늘려서 계산해본다. 더 큰 간격으로도 설치가 될 수 있을수도 있으니깐.
        answer = mid
    else: # 설치할 수 있는 공유기 수가 C미만이면 간격을 줄여서 설치해본다.
        end = mid-1

print(answer)

