def solution(elements):
    lst = elements*2
    length = len(elements)
    result = set()
    for i in range(length):
        for j in range(length+i):
            result.add(sum(lst[j:j+i+1]))
    return len(result)
            
    