def solution(k, tangerine):
    cnt = {}
    for size in tangerine:
        cnt.setdefault(size, 0)
        cnt[size] += 1
    sorted_cnt = sorted(cnt.values(), reverse=True)
    box = 0
    for i in range(len(sorted_cnt)):
        box += sorted_cnt[i]
        if box>=k: return i+1