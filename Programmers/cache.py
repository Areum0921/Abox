# 4가지 경우를 생각
# 캐시에 빈칸 남아있고, 캐시에 있는 정보 or 캐시에 없는 정보
# 캐시가 꽉차 있고, 캐시에 있는 정보 or 캐시에 없는 정보
def solution(cacheSize, cities):
    answer = 0
    cache=[]

    if cacheSize==0:
        return 5*len(cities)
    for i in cities:
        i=i.upper() # 대소문자 구분을 안하기때문에 대문자로 통일
        print(cache, answer)
        if len(cache)<cacheSize: # 빈 캐시 칸이 있을때
            if i not in cache: # 캐시에 없는 정보일때
                cache.append(i)
                answer+=5
            else: # 캐시에 있는 정보일때
                cache.remove(i) # 캐시 최근성 업데이트
                cache.append(i)
                answer+=1
        elif len(cache)==cacheSize:
            if i in cache:
                cache.remove(i) # 캐시 최근성 업데이트
                cache.append(i) # 최근 사용 캐시
                answer+=1
            else:
                cache.pop(0) # 사용한지 제일 오래된거
                cache.append(i)
                answer+=5

    print(answer)
    return answer

cacheSize=5
#cities=["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
#cities=["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
cities=["SEOUL","SEOUL","SEOUL"]
solution(cacheSize,cities)