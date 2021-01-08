
def solution(progresses, speeds):
    cnt_progess=len(progresses)
    count=[0]*len(progresses)
    pro_num=0
    result=0
    answer = []
    while(1):

        for i in range(len(progresses)):
            progresses[i]=progresses[i]+speeds[i]
            if(progresses[i]>=100 and count[i]==0):
                count[i]=1

        result=0
        while(1):
            if(pro_num>len(progresses)-1):
                if(result!=0):
                    answer.append(result)
                break
            elif(progresses[pro_num]>=100 and count[pro_num]==1):
                result=result+1
                count[pro_num]=2
                pro_num=pro_num+1

            else:
                if(result!=0):
                    answer.append(result)
                break
        if(min(count)==2):
            break

    return answer

