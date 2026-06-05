def solution(k, score):
    answer = []
    lst = []
    for x in score:
        lst.append(x)
        lst.sort(reverse=True)
        if len(lst)>k: lst = lst[:k]
        answer.append(lst[-1])
    
    return answer