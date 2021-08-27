# 문자열 내에서 규칙에 맞는 연속된 부분 문자열을 구할때는 l,r 투 포인터를 이용해보자.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0

        answer = 0
        l = 0
        check = {}

        for r, chr in enumerate(s):
            if chr in check and l <= check[chr]:
                l = check[chr] + 1
            else:
                answer = max(answer, r - l + 1)
            check[chr] = r

        return answer