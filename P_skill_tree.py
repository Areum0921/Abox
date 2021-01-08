def solution(board, moves):
    answer = 0
    stack_list=[] # 쌓인 블록 리스트
    size=len(board)
    for i in moves:
        j=0
        while(1):
            if(j==size):
                break
            elif(board[j][i-1]!=0): #이동 시킬 위치
                stack_list.append(board[j][i-1])
                board[j][i-1]=0 #이동 시켜서 해당칸은 빈칸으로
                break
            elif(board[j][i-1]==0):
                j=j+1
        if(len(stack_list)>1): # 옮긴 블럭이 2개 이상일때
            if(stack_list[-1]==stack_list[-2]): #맨위,그아래가 같은 블록일때 삭제
                del stack_list[-2:]#맨뒤에서 2개 삭제
                answer=answer+2 #한번 터질때 2개씩이니까
   
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves=[1,5,3,5,1,2,1,4]	
board
solution(board, moves)
