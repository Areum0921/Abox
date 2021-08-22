# 2가지.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if str(x)[::-1]==str(x):
            return True

        return False

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s[::-1]==s
