def GCD(x, y):
    while y!=0:
        x, y = y, x%y
    return x

def solution(arr):
    b = arr[0]
    for i in range(1, len(arr)):
        a = arr[i]
        b = a*b//GCD(a, b)
    return b