# 트리 구현에 대해 배웠다.
# 기존문제 전위, 후위 + 중위
import sys
sys.setrecursionlimit(10**6)

class Tree:

    def __init__(self):
        self.parent = None # 부모 노드
        self.left = None # 자식 왼쪽
        self.right = None # 자식 오른쪽
        self.data = None # 노드 정보 값
        self.index = None # 노드 번호

def pre(root, vector): # 전위 부모, 왼, 오
    if root == None:
        return vector

    vector.append(root.index)
    pre(root.left, vector)
    pre(root.right, vector)

    return vector

def post(root, vector): # 후위 왼,오,부모
    if root == None:
        return vector

    pre(root.left, vector)
    pre(root.right, vector)
    vector.append(root.index)

    return vector

def inOrder(root, vector): # 중위, 왼,부모,오
    if root == None:
        return vector

    inOrder(root.left,vector)
    vector.append(root.index)
    inOrder(root.right,vector)

    return vector

def solution(nodeinfo):
    answer = [[]]
    root = None
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1) # 노드 번호 추가
    nodeinfo = sorted(nodeinfo, key=lambda x: -x[1]) # y좌표 기준 정렬

    for i, node in enumerate(nodeinfo):
        makeTree=Tree()
        makeTree.index = node[2] # 노드 번호
        makeTree.data = node

        if root == None:
            root = makeTree
        else:
            cur = root
            while 1:
                if cur.data[0] < makeTree.data[0]: # root보다 x좌표가 크면 오른쪽
                    if cur.right == None: # 비어있으면 root에 오른쪽 자식으로 넣기
                        cur.right = makeTree
                        makeTree.parent = cur # makeTree의 부모는 root
                        break
                    else: # root의 오른쪽이 비어있지 않으면
                        cur = cur.right # 현재 root의 오른쪽자식으로 이동후 다시 자리 탐색
                else:
                    if cur.left == None:
                        cur.left = makeTree
                        makeTree.parent = cur
                        break
                    else:
                        cur = cur.left

    answer = [pre(root,[]),post(root,[]),inOrder(root,[])]

    print(answer)
    return answer

nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
solution(nodeinfo)