def check(x, y, park, n):
    if x+n>=len(park) or y+n>=len(park[0]): return 0
    for i in range(n+1):
        if park[x+n][y+i] != "-1" or park[x+i][y+n] != "-1": return 0
    m = check(x, y, park, n+1)
    return m+1

def solution(mats, park):
    mx = 0
    mats.sort(reverse=True)
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] != "-1":
                print("0", end=' ')
                continue
            n = check(i, j, park, 0)
            print(n, end=' ')
            mx = max(n, mx)
        print()
    for mat in mats:
        if mat<=mx: return mat
    return -1