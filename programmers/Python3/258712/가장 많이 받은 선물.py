def solution(friends, gifts):
    length = len(friends)
    gave = {friend:dict(zip(friends, [0]*length)) for friend in friends}
    for gift in gifts:
        a, b = gift.split()
        gave[a][b] += 1
    
    give = dict(zip(friends, [0]*length))
    for i in range(length-1):
        for j in range(i+1, length):
            a, b = friends[i], friends[j]
            x, y = gave[a][b], gave[b][a]
            if x>y: give[a]+=1
            elif x<y: give[b]+=1
            else:
                get_point = lambda n: sum(gave[n].values()) - sum(gave[friend][n] for friend in friends)
                nx, ny = get_point(a), get_point(b)
                if nx>ny: give[a]+=1
                elif nx<ny: give[b]+=1
    return max(give.values())