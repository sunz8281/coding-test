def solution(s):
    i = 0
    answer = 0
    while i<len(s):
        answer+=1
        c = s[i]
        same, not_same = 0, 0
        while i<len(s):
            if c==s[i]: same+=1
            else: not_same+=1
            i+=1
            if same==not_same:
                break
    return answer