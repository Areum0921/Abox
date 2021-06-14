def solution(A):

    if len(A)<1:
        return 0
    buy=A[0]
    profit=0
    for i in range(1,len(A)):
        if buy>A[i]:
            buy=A[i]
            continue
        else:
            print(A[i], buy)
            profit=max(profit,A[i]-buy)
            print("new",profit)

    print(profit)
    return profit


A=[23171,21011,21123,21366,21013,21367]
solution(A)