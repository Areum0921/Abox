# 80%, 59%
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if len(needle) == 0:
            return 0

        if needle in haystack:
            return haystack.index(needle) # needle이 haystack에서 시작되는 인덱스 위치.
        else:
            return -1