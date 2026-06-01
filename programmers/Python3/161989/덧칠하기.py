def solution(n, m, section):
    last = 0
    answer = 0
    for x in section:
        if last>x: continue
        answer+=1
        last = x+m
    return answer