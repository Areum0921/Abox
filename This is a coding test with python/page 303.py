# 얕은 복사 A->B - 새 객체 B가 생성되어 복사하고자 하는 값들(A)을 참조 하여 복사된다.
# A가 변경되면 B도 변경된다.
# 깊은 복사 - 필드가 역 참조 된다.
# 얕은 복사 처럼 A의 값을 참조하는 대신, 참조가 되는 모든 객체를 위한 새 객체를 만든다.
# A가 변경되어도 B는 변경되지 않는다.

# a=[1,2,3]일때
# b=a
# c=copy.deepcopy(a)
# a = [1,2,3], b=[1,2,3], c=[1,2,3] 이다.
# a.append(6)을 수행했을경우
# a = [1,2,3,6], b=[1,2,3,6], c=[1,2,3] 이다.
# 얕은복사는 복사한 원래 객체에 따라 영향을 받고, 깊은 복사는 아예 새로운 객체라 보면된다.
from collections import deque
import copy
v= int(input())

indegree=[0]*(v+1) # 진입 차수

graph=[[] for _ in range(v+1)]

time=[0] * (v+1)
print(graph)

for i in range(1,v+1): # 강의에 대한 정보
    data = list(map(int,input().split(" "))) # i번 강의의 시간, 이후로 이 강의를 듣기 위한 선수 강의 번호
    time[i]=data[0] # i번 강의 수강 시간
    for j in data[1:-1]: # i번 강의를 듣기 위한 선수 강의
        indegree[i] +=1
        graph[j].append(i) # j를 들어야 i 가능.

def topology_sort():
    result=copy.deepcopy(time) # 시간 깊은 복사 # 해당 강의 시간은 기본값.
    q=deque()

    for i in range(1,v+1):
        if indegree[i]==0: # 선행 과목이 없는 강의들
            q.append(i)
    print(result)
    print(graph) # graph[i]에는 i를 선수강의를 가진 강의번호들
    print(time) # 해당 강의들의 강의 시간.
    while q:
        now = q.popleft()

        for i in graph[now]:
            print(result[i],result[now]+time[i],i,now)
            result[i]=result[now]+time[i] # i번 수강시간은 now번째 강의 수강시간 + i번 강의 수강시간
            # 선수 과목이 선택이아니라 모두 들어야 하므로 max 안쓰고 result[now]+time[i]를 저장해 나가도된다.
            # 만약 3번강의의 선수과목이 1 or 2 라면 골라야 하겠지만
            # 1 and 2라면 3번 강의의 총 시간은 1번강의(선수과목포함) + 2번강의(선수과목포함) + 3번강의 시간이 되기 때문
            indegree[i]-=1
            if indegree[i]==0: # 선수 과목 모두 수강한 상태
                q.append(i)

    print(result)

topology_sort()