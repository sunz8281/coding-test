def solution(n):
    left, right = 1, 2
    answer = 0
    while left<=n:
        hap = sum(i for i in range(left, right))
        if hap>n: left +=1
        elif hap<n: right += 1
        else:
            answer += 1
            right += 1
    return answer