# 96.96%, 75.99%
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_str = ""
        answer = []
        for i in digits:
            digits_str += str(i)

        digits_str = str(int(digits_str) + 1)

        for i in digits_str:
            answer.append(int(i))

        return answer