def solution(players, callings):
    grade = {}
    
    for i in range(len(players)):
        grade[players[i]] = i
    
    for current in callings:
        x = grade[current]
        prev = players[x-1]
        players[x], players[x-1] = prev, current
        grade[prev], grade[current] = x, x-1
    return players