
class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        answer = 0

        for i in range(1, len(s)):
            if dict[s[i]] <= dict[s[i - 1]]:  # 앞문자가 더 크거나 같으면 +
                answer += dict[s[i - 1]]
            else:  # 앞문자가 작으면 -
                answer -= dict[s[i - 1]]

        answer += dict[s[-1]]  # 마지막 문자 처리. 마지막 문자는 무엇이오든 +로 처리가능.

        return answer

# 2번째 풀이
# 1과 5를 이용해 4, 1과 10을 이용해 9를 만들 수 있음. 3은 IIX가 아닌 III임.
class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        p_dict = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM': 900} # 특수 숫자 처리.
        answer = 0

        for i in p_dict: # p_dict에 해당하는 문자가 존재하면 더해주고, 해당 문자 s에서 삭제
            if i in s:
                answer += p_dict[i]
                s = s.replace(i,"")
        for i in s:
            answer += dict[i]


        return answer