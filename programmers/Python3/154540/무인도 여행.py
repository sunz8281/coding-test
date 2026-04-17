from collections import deque 

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

def solution(maps):
    answer = []
    n, m = len(maps), len(maps[0])
    for i in range(n):
        for j in range(m):
            if maps[i][j]=='X': continue
            q = deque([(i, j)])
            answer.append(0)
            while q:
                x, y = q.popleft()
                if maps[x][y]=='X': continue
                answer[-1] += int(maps[x][y])
                maps[x] = maps[x][:y] + 'X' + maps[x][y+1:]
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if not(0<=nx<n and 0<=ny<m):
                        continue
                    q.append((nx, ny))
    if not answer: return [-1]
    return sorted(answer)