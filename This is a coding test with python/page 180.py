# 성적이 낮은순서대로 학생이름

def rank(array):

    array=sorted(array,key=lambda x : x[1]) # 성적부분에 해당하는 각 배열의 인덱스 1번을 기준으로 오름차순 정렬

    for i in array:
        print(i[0],end=" ")


array=[['홍길동',95],['이순신',77]]
rank(array)