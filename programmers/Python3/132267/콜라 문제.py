def solution(a, b, n):
    mod = 0
    answer=0
    while n:
        mod, n=(n+mod)%a,(n+mod)//a*b
        answer+=n
    return answer