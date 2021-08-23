class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)  # 길이순 정렬
        answer = ''
        for i in range(len(strs[0])):
            temp = strs[0][i]
            for j in range(len(strs)):
                if temp != strs[j][i]:
                    return answer

            answer+=temp

        return answer

# 속도 상위권은 startswith를 사용했다. 사용해보기.
# str1.startswith(str2)는 str1이 str2로 시작하는지 검사할수있음.
# ex) a = "ab", b = "abc", c="bcd"일때
# b.startswith(a) = True, c.startswith(a) = False

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in strs:
            while not i.startswith(strs[0]):
                strs[0] = strs[0][:-1]

        return strs[0]