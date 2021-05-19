# 양쪽 끝 처리만 해주면 나머지는 간편하게
# max([i][j-1],[i][j])를 더해나가면 된다.

def solution(triangle):
    answer = 0
    maxnum=0

    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            if j==0: # 왼쪽끝
                triangle[i][j]+=triangle[i-1][j]
            elif j==len(triangle[i])-1: # 오른쪽 끝
                triangle[i][j] += triangle[i - 1][j-1]
            else: # 가운데 부분
                triangle[i][j] += max(triangle[i-1][j],triangle[i-1][j-1])
    print(triangle)
    answer =max(triangle[-1]) # 위에서부터 높은값을 선택하여 더해왔을때 마지막 리스트에서 가장 큰 값 뽑기.
    print(answer)
    return answer

triangle=[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
solution(triangle)