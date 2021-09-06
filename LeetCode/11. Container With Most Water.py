class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0
        l,r = 0,len(height)-1 # 2포인터

        while l<r:
            answer = max(answer,(r-l)*min(height[l],height[r])) # 용량

            if height[l]>=height[r]: # 왼쪽이 더 높거나 같으면 오른쪽 옮겨보기
                r -= 1
            else:
                l += 1

        return answer