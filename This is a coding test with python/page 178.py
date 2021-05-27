# 내림차순 정렬

def sort1(array):
    array=sorted(array, reverse=True)

    print(' '.join(map(str,array)))

array=[15,27,12]

sort1(array)