def solution(wallet, bill):
    wallet.sort()
    a, b = sorted(bill)
    answer = 0
    while a>wallet[0] or b>wallet[1]:
        b = b//2
        a, b = sorted((a, b))
        answer += 1
    return answer