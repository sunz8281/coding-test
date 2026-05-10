import heapq

def solution(n, works):
    q = [-x for x in works]
    heapq.heapify(q)
    for i in range(n):
        x = heapq.heappop(q)
        heapq.heappush(q, min(0, x+1))
    return sum([x**2 for x in q])