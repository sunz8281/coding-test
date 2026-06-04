def solution(s):
    result = [-1]*len(s)
    for i in range(1, len(s)):
        for j in range(i):
            if s[i] != s[j]: continue
            result[i] = i-j
    return result