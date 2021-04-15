def solution(record):
    answer = []
    dict={}
    for i in range(len(record)):
        record[i]=record[i].split(' ')

    for i in range(len(record)):
        if(record[i][0]=='Enter' or record[i][0]=='Change'):
            dict[record[i][-2]]=record[i][-1]
        #elif(record[i][0]=='Leave'):
         #   del dict[record[i][-1]]

    for i in range(len(record)):
        if(record[i][0]=='Enter'):
            answer.append(dict[record[i][-2]]+"님이 들어왔습니다.")

        elif(record[i][0]=='Leave'):
            answer.append(dict[record[i][-1]]+"님이 나갔습니다.")

    return answer