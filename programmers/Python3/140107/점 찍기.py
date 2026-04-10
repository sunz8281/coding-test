def solution(k, d):
    answer = 0
    x = k*(d//k)
    for i in range(0,d+1,k):
        while x>=0 and i**2 + x**2 > d**2:
            x-=k
        answer += x//k+1
    return answer