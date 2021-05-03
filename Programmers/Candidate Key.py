# 모든 컬럼의 조합을 구하고, 유일성이 확보된 조합 모두 저장 그 다음에 최소성으로 한번더 걸러줌
# 최소성 부분에서 애먹었다..
# 찾아 보니 issubset이라는 좋은 내장 함수가 있었다.
# issubset 쓰니까 금방임..

from itertools import combinations

def solution(relation):
    ans = []
    all=[]
    for i in range(1, len(relation[0])+1):
        for j in combinations(range(0,len(relation[0])),i):
            all.append(j)

    for i in all: # 모든 조합에 대해서
        check=[[] for _ in range(len(relation))] # 1컬럼 조합, 2컬럼조합, 3컬럼조합,... n컬럼 조합
        for j in i:
            for k in range(len(relation)):
                check[k].append(relation[k][j])
        check2=[] # check 중복되는값 빼고 저장하기
        for m in check:
            if(m not in check2):
                check2.append(m)
        #print(check,check2,len(check),len(check2))
        if len(check)==len(check2): # 중복된거 제거작업후에도 길이가 같으면 유일성 충족
            ans.append(i) # 유일성 확보된 조합 저장

    for i in ans: # 유일성이 확보된 모든 경우
        #print("22333",i)
        for j in ans[:]: # i에 대해서 부분집합
            # ( ans[:]로 해야 remove한게 반영된다.)
            if i==j:
                continue
            if set(i).issubset(set(j)): # i가 j에 대해서 부분집합이면 j삭제, 최소성을 만족하지 않기때문에
                #
                print(set(i),set(j))
                ans.remove(j)
            print(ans)
    #그러면 부분집합이 아닌 유일성 키만 남게된다.
    print(len(ans))
"""
    for i in ans:
        minnum = True
        for j in range(len(i)):
            for k in range(len(answer)):
                if(i[j].issubset(answer[k])):
                    minnum=False
        if(minnum==True):
            answer.append(i)
        print(answer)
"""







#relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
#solution(relation)
solution([['a',1,'aaa','c','ng'],['b',1,'bbb','c','g'],['c',1,'aaa','d','ng'],['d',2,'bbb','d','ng']])