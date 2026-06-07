def solution(ingredient):
    answer = 0
    stack = []
    for x in ingredient:
        stack.append(x)
        while stack[-4:] == [1, 2, 3, 1]: 
            answer += 1
            for i in range(4): del stack[-1]
    return answer