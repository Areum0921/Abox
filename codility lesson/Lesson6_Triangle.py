# 숫자들을 오름차순 정렬해서 앞의 숫자 2개의 합보다 작으면 조건에 만족함.
# 만족하는 숫자들의 인덱스 출력.
# 3개의 숫자중 작은값,중간값 2개를 더해 제일 큰값보다 크면
# 작은값+큰값 > 중간값, 중간값+큰값 > 작은값은 당연히 성립하게 된다.
# O(n log n)
def solution(A):
    new_A=[]
    answer=[0]
    for i,j in enumerate(A):
        new_A.append([j,i]) # 값, 인덱스

    new_A.sort()


    for i in range(2,len(new_A)):
        if new_A[i-2][0]+new_A[i-1][0]>new_A[i][0]:
            answer=[new_A[i-2][1],new_A[i-1][1],new_A[i][1]]
            return answer


A=[10,2,5,1,8,20]
solution(A)