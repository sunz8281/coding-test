def solution(keymap, targets):
    min_click = dict()
    for key in keymap:
        for i, alpha in enumerate(key):
            if alpha not in min_click: min_click[alpha] = i+1
            else: min_click[alpha] = min(min_click[alpha], i+1)
    answer = []
    for target in targets:
        n = 0
        for alpha in target:
            if alpha not in min_click:
                n = -1
                break
            n += min_click[alpha]
        answer.append(n)
    return answer