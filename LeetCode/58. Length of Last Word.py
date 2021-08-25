# 52%, 35%
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cnt = 0

        for i in range(len(s) - 1, -1, -1): # 뒤에서부터
            if s[i] == " " and i < len(s) - 1: # 맨마지막이 아닌경우
                if s[i + 1] != " ": # 공백 뒤에 문자가 존재하면
                    break
            if s[i] != " ":
                cnt += 1

        return cnt


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new_s = s.split(" ")

        for i in range(len(new_s) - 1, -1, -1):
            if len(new_s[i]) != 0:
                return len(new_s[i])