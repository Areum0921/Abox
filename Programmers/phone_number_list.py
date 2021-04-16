# sort를 이용하면 현재 번호와 나머지번호를 모두 비교할 필요가없음 -> 이중 for문 사용 안해도가능!
# ex) '112','119','1123,'1213'
# sort하면 '112', '1133','1213','119','1192'
# 112 113 비교 / 113 121 비교 / 121 119 비교 / 119 119 비교
# 바로 뒤 번호만, 앞번호의 길이만큼 비교하면 된다.
def solution(phone_book):
    answer = True
    length=len(phone_book) # 전화번호 개수
    phone_book.sort() # 정렬
    for i in range(length):
       if(phone_book[i] in phone_book[i+1][:len(phone_book[i])]):
           return False

    return answer

phone_book=["12","123","1235","567","88"]
solution(phone_book)


"""
정확성은 통과, 효율성 실패
def solution(phone_book):
    answer = True
    length=len(phone_book) # 전화번호 개수
    for i in range(length):
        for j in range(i+1,length):
            if(phone_book[i]==phone_book[j][:len(phone_book[i])]):
                #확인할 숫자 길이 만큼 접두어 확인
                return False
            
    return answer
"""