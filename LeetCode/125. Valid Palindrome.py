class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ''

        for i in s:
            if i.isalpha():  # 알파벳
                new_str += i.lower()  # 소문자로
            if i.isdigit():  # 숫자
                new_str += i

        print(new_str)
        return new_str == new_str[::-1]