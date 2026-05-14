def solution(n):
    a, b = 0, 1
    for i in range(n-1):
        temp = b
        b = a+b
        a = temp
    return b%1234567