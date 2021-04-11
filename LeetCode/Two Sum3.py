"""
476ms -> 76ms 속도를 개선했음에도 속도 순위 꽤 하위권, 상위권 코드를 보니 enumerate 함수를 이용
enumerate 함수는 리스트를 인덱스 : 해당 인덱스의 값 으로 나타내준다.
enumerate = O(n)
56ms

"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check={}
        for NumIndex, Num in enumerate(nums):
            if(Num in check): # 현재 숫자가 check에 있으면
                return [check[Num],NumIndex]
            check[target - Num] = NumIndex # check의 [target-Num] 인덱스에 현재 인덱스값을 저장한다.
            # [2,7,11,15] target=26일때
            # 26-2 = check[24]에 2의 인덱스 0을 넣는다.
            # check[7]은 존재하지 않는다.
            # 26-7 = check[19]에 7의 인덱스 1을 넣는다.
            # check[11]은 존재하지 않는다.
            # 26-11 = check[15]에 11의 인덱스 2를 넣는다.
            # check[15]는 존재한다. 즉, target-앞의 어떤 숫자=15가 있다는 뜻.
            # 15와 check[15]에 들어있는 인덱스 위치(2)의 숫자(nums[2])를 더하면 26이된다.
            # check[15]=2, 15의 numIndex는 3

