from collections import deque 

def check_top(current, q):
    for item in q:
        if item[0]>current[0]:
            return False
    return True

def solution(priorities, location):
    q = deque([(x, i) for i, x in enumerate(priorities)])
    turn = 0
    while q:
        current = q.popleft()
        if not check_top(current, q):
            q.append(current)
            continue
        turn += 1
        if current[1] == location: return turn