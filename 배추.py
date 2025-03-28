from collections import deque

# 2
# 10 8 17
# 0 0
# 1 0
# 1 1
# 4 2
# 4 3
# 4 5
# 2 4
# 3 4
# 7 4
# 8 4
# 9 4
# 7 5
# 8 5
# 9 5
# 7 6
# 8 6
# 9 6
# 10 10 1
# 5 5

import sys

T = int(input())
ans=[]

for _ in range(T):
    n,m,num = map(int, sys.stdin.readline().split())
    graph = [[0 for _ in range(50)] for _ in range(50)]

    for _ in range(num):
        a, b = map(int, sys.stdin.readline().split())
        graph[a][b] = 1

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    visit = set()
    visit.add((0,0))

    cnt = 0
    dq = deque()

    for i in range(n):
        for j in range(m):
        
            if (i,j) not in visit and graph[i][j]==1 :


                visit.add((i,j))

                cnt +=1 
                dq.append([i,j, cnt])

                while dq:

                    x, y, cnt = dq.popleft()    

                    for k in range(4):

                        nx = x + dx[k]
                        ny = y + dy[k]

                        # ** 중요 **
                        if nx < 0 or ny<0 or nx>=n or ny>=m :
                            continue

                        if (nx,ny) not in visit and graph[nx][ny]== 1 :

                            visit.add((nx,ny))
                            dq.append([nx,ny,cnt])

    ans.append(cnt)

for i in ans:
    print(i)
