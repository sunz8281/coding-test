def solution(players, m, k):
    servers = [0]*len(players)
    cnt = 0
    for i in range(len(players)):
        add = max(0, players[i]//m-servers[i])
        cnt += add
        for j in range(k):
            if i+j>=len(players): continue
            servers[i+j] += add
    return cnt