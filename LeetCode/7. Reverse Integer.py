class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = x * -1
            answer = int(str(x)[::-1]) * -1
            if answer < -2 ** 31:
                return 0
        else:
            answer = int(str(x)[::-1])
            if answer >= 2 ** 31:
                return 0

        return answer