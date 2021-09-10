class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        answer = [[1] for _ in range(rowIndex + 1)]

        for i in range(1, rowIndex + 1):
            for j in range(i + 1):
                if j == i:
                    answer[i].append(1)
                elif j != 0:
                    answer[i].append(answer[i - 1][j] + answer[i - 1][j - 1])

        return answer[rowIndex]