def solution(N, A):
    counter = [0] * (N + 1)
    max_count=0
    number=0
    for i in A:
        # maxconter 발생시 매번 갱신 x
        if i == N + 1:
            number = max_count
        else:
            if counter[i]<number: # max_counter 발생이후, number보다 작으면
                # counter[i]를 number로 바꾼후, +=1
                counter[i]=number

            counter[i] += 1

            if max_count<counter[i]:
                max_count=counter[i]
        #print(counter)

    for i in range(len(counter)):
        if counter[i]<number:
            counter[i]=number

    #print(counter[1:])
    return counter[1:]

A=[3,4,4,6,1,4,4]
N=5
solution(N,A)