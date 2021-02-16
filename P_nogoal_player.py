def solution(participant, completion):
    answer = ''

    participant.sort()
    completion.sort()
    i=0
    while(len(participant)):
        
        if(i==len(participant)-1):
            answer=participant[i]
            break
            
        elif(participant[i] != completion[i]):
            answer = participant[i]
            break
        i=i+1
        
        
            
    
    print("result :",answer)  
    return answer

participant =["leo", "kiki", "eden"]
completion =["eden", "kiki"]
solution(participant, completion)

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
solution(participant, completion)
