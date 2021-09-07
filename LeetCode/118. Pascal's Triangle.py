class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = [[1] for _ in range(numRows)]

        for i in range(1, numRows):
            for j in range(i + 1):
                if j != 0 and j != i:  # 중간부분
                    answer[i].append(answer[i - 1][j - 1] + answer[i - 1][j])
                elif j == i:  # 맨끝
                    answer[i].append(1)

        return answer