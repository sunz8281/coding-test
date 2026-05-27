from collections import deque

def solution(s):
    mapping = {")": "(", "]": "[", "}": "{"}
    
    q = deque(list(s))
    length = len(s)
    answer = 0
    for i in range(length):
        flag = 0
        stack = []
        for c in q:
            if c in mapping.values():
                stack.append(c)
            elif stack and stack[-1] == mapping[c]:
                stack.pop()
            else:
                flag = 1
                break
        if not (flag or stack): answer += 1
        q.append(q.popleft())
    return answer