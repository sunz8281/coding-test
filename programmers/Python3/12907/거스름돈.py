def solution(n, money):
    dp = [0] * (n+1)
    dp[0] = 1
    money.sort()
    for cash in money:
        for i in range(cash, n+1):
            dp[i] += dp[i-cash]
    return dp[n]