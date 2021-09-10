class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 10001
        sell = 0

        for i in prices:
            if buy > i:  # 지금 구매한가격보다 더 싼 가격이면
                buy = i

            if sell < i - buy:  # 기존 이익보다 지금 팔때 이익이 더 크면
                sell = i - buy

        return sell