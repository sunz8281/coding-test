def solution(brown, yellow):
    for i in range(1, (yellow+1)//2+1):
        if yellow%i==0:
            x, y = i+2, yellow//i+2
            if x*2 + y*2 - 4 == brown: return [y, x]