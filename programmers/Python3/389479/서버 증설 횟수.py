def solution(players, m, k):
    servers = [[0, 0] for i in range(len(players))]
    cnt = 0
    for i in range(len(players)):
        add = max(0, players[i]//m-servers[i][0])
        cnt += add
        for j in range(k):
            if i+j>=len(players): continue
            servers[i+j][0] += add
    return cnt