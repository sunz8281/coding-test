def solution(food):
    left = ''.join(str(i)*(food[i]//2) for i in range(len(food)))
    return left + '0' + left[::-1]