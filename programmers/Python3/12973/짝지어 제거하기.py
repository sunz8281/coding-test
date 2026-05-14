def solution(s):
    stack = []
    for c in s:
        stack.append(c)
        while len(stack)>=2 and stack[-1]==stack[-2]:
            del stack[-1]
            del stack[-1]
    if stack: return 0
    return 1