def solution(A):
    right={} # 오른쪽
    left={} # 왼쪽
    # 나눠서 계산.

    for i in A: # 각 숫자들이 몇번씩 등장했는지 체크하기.
        if i in right:
            right[i] += 1
        else:
            right[i]=1

    cnt=0

    left_leader=0 # 현재 빈도수가 가장 많은 숫자
    left_length=0 # 요소 개수
    left_leader_cnt=0 # 현재 가장 많은 빈도수

    right_length = len(A)

    for i in range(len(A)):
        right[A[i]]-=1 # 오른쪽에서 A[i]데이터에 대한 내용 -1씩
        right_length-=1

        if A[i] in left: # 왼쪽으로 옮기기
            left[A[i]] += 1
        else:
            left[A[i]]=1
        #print(left,A[i],right,left_length)

        left_length+=1

        #print(left,right,left[A[i]],A[i])
        if left[A[i]] > left_leader_cnt: # left에서 A[i]빈도수가 left_leader_cnt보다 높으면 갱신
            left_leader=A[i] # 현재 A[i]가 제일 많이 나옴
            left_leader_cnt=left[A[i]] # 제일 많이 나온 횟수는 left[A[i]]

        if right[left_leader]>right_length//2 and left_leader_cnt>left_length//2:
            # 오른쪽에서 left_leader에 해당하는 숫자의 빈도수가 오른쪽 요소 절반 초과고
            # 왼쪽 left_leader의 빈도수가 왼쪽 요소 절반 초과일때

            cnt+=1

    print(cnt)
    return cnt


A=[4,3,4,4,4,2]
solution(A)
