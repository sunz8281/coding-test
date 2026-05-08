def solution(players, m, k):
    servers = [[0, 0] for i in range(len(players))]
    for i in range(len(players)):
        add = max(0, players[i]//m-servers[i][0])
        servers[i][1] = add
        for j in range(k):
            if i+j>=len(players): continue
            servers[i+j][0] += add
    print(servers)
    cnt = 0
    for server in servers:
        cnt += server[1]
    return cnt