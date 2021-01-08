def solution(n, lost, reserve):
    lost2=set(lost)-set(reserve)#잃어버린애중 여벌있는애 제외
    reserve2=set(reserve)-set(lost)#여유분있는애중 잃어버린애 제외
    
    for i in lost2:
        print(lost2,reserve2,n)
        if i+1 in reserve2: #잃어버린애 뒷번호가 여유있으면
            reserve2.remove(i+1)
        elif i - 1 in reserve2:#잃어버린애 앞번호가 여유있으면
            reserve2.remove(i - 1)
        else:
            n=n-1
    answer = 0
    print(lost2,reserve2,n)
              
        
             
                
    
    return answer

n=5
lost=[2,4]
reserve=[1,2,3]
solution(n, lost, reserve)
