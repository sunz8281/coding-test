def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    answer = 0
    for i in range(min(len(A), len(B))):
        answer += A[i]*B[i]

    return answer