def solution(d,budget):
    d_sort=d.sort()
    result=0
    sum_budget=0
    i=0
    while(1):
        print(sum_budget,d,budget)
        if(i<len(d)):
            sum_budget+=d[i]
            if(budget>=sum_budget):
                result+=1
            elif(budget<sum_budget):
                break
            i+=1
        else:
            break
    return result

def solution2(d,budget):
    d.sort()
    result=0
    i=0
    while(1):
        print(budget)
        if(i<len(d)):
            budget-=d[i]
            if(budget>=0):
                result+=1
            else:
                break
        else:
            break
        i+=1
    print(result)
    return result

d=[1,3,2,5,4]
budget=9
solution2(d,budget)