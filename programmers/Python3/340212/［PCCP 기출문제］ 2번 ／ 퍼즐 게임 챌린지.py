def solution(diffs, times, limit):
    left, right = 0, max(diffs)
    while left<right-1:
        level = (left+right+1)//2

        time_prev = 0
        time = 0
        for i in range(len(diffs)):
            time_cur = times[i]
            if diffs[i]>level: time += times[i] + (times[i] + time_prev) * (diffs[i]-level)
            else: time += times[i]
            time_prev = time_cur

        if time>limit: left = level
        else: right = level
    return right