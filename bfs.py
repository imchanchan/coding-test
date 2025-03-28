from collections import deque

import sys

"""
첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하인 양의 정수이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다. 
둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.

입력
7
6
1 2
2 3
1 5
5 2
5 6
4 7

출력
4
"""

n = int(input())
k = int(input())
arr = []

# 입력받기 1 2 / 3 4
arr = [list(map(int, input().split())) for i in range(k)]

# 그래프 이차원 배열 만들기!
graph = [[0 for _ in range(n+1)] for _ in range(n+1)]

# 1. 그래프 만들기
for i, j in arr:
    graph[i][j] = 1
    graph[j][i] = 1

# 2. 방문 노드 만들기
visit = set()
q = deque()
q.append(1)
visit.add(1)


ans=0
# bfs
while q:

    x = q.popleft()
    
    for i in range(1, n+1):
        if graph[x][i] ==1 and i not in visit:

            q.append(i)
            visit.add(i)

            ans +=1


print(ans)
