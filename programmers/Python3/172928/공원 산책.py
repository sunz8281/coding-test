dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
idx = {'N':0, 'S':1, 'W':2, 'E':3}

def solution(park, routes):
    x, y = 0, 0
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S': x, y = i, j
    for route in routes:
        d, n = route.split()
        dist = idx[d]
        nx, ny = x+dx[dist]*int(n), y+dy[dist]*int(n)
        if 0<=nx<len(park) and 0<=ny<len(park[nx]) and 'X' not in [park[i][j] for i in range(min(x, nx), max(x, nx)+1) for j in range(min(y, ny), max(y, ny)+1)]:
            x, y = nx, ny
    return [x, y]