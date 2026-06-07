def solution(number, limit, power):
    divisors_cnt = [0]*(number+1)
    for i in range(1, number+1):
        for j in range(i, number+1, i):
            divisors_cnt[j] += 1
    answer = 0
    for i in range(1, number+1):
        answer += divisors_cnt[i] if divisors_cnt[i]<=limit else power
    return answer