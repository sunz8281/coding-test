# from, sub, to / a에서 c로 n개의 원판을 옮기는데 b를 서브로 사용
def hanoi(n, a, b, c):
    if n<=0: return []
    
    prev = hanoi(n-1, a, c, b)
    
    mid = [[a, c]]
    
    after = hanoi(n-1, b, a, c)
    
    return prev + mid + after

def solution(n):
    return hanoi(n, 1, 2, 3)