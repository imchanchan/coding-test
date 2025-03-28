from collections import deque

def solution(maps):
    
    dq = deque()    
    dq2 = deque()
    visit = set()
    visit2 = set()
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            
            if maps[i][j] =='S':
                dq.append([i,j, 0])
                visit.add((i,j))
          
    # bfs
    while(dq):
        x, y, cnt = dq.popleft()
        
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx<0 or ny<0 or nx>=len(maps) or ny>=len(maps[0]) or (nx,ny) in visit: 
                continue
                
            if maps[nx][ny]=='O' or maps[nx][ny]=='E':
                dq.append([nx, ny, cnt+1])
                visit.add((nx,ny))
                
            if maps[nx][ny] == 'L':
                dq2.append([nx, ny, cnt])
                break 
                
        print(f"dq" ,dq)

    # bfs2
    while dq2 :
        x, y, cnt = dq2.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx<0 or ny<0 or nx>=len(maps) or ny>=len(maps[0]) or (nx,ny) in visit2: 
                continue
                
            if maps[nx][ny]=='O':
                dq.append([nx, ny, cnt+1])
                visit2.add((nx,ny))
                
            if maps[nx][ny] == 'E':
                return cnt


print(solution(["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]))