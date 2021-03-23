from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for i in course: # 코스에 따라
        menu=[]
        for j in orders: # 주문메뉴
            for k in combinations(j,i): # 해당 주문 메뉴로 구성할수있는 i개 품목 코스 조합 구성
                str1=''.join(sorted(k))
                menu.append(str1)
        sorted_menu=Counter(menu).most_common() # 주문 수 높은순정렬
        for m in range(len(sorted_menu)):
            if(sorted_menu[m][1]>=sorted_menu[0][1] and sorted_menu[0][1]>1):
                # 제일 주문횟수많은 코스기준으로 주문횟수 같으면서, 해당 코스의 최대 주문횟수가 2부터일때
                answer.append(sorted_menu[m][0])
    answer.sort()
    return answer

orders=["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course=[2,3,5]
solution(orders,course)