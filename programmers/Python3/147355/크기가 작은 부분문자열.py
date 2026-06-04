def solution(t, p):
    window = len(p)
    cnt = 0
    p = int(p)
    for i in range(len(t)-window+1):
        x = t[i:i+window]
        if int(x)<=p: cnt += 1
    return cnt
        