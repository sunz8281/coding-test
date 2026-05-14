def solution(s):
    zero_cnt = 0
    cnt = 0
    while s!="1":
        zero = s.count("0")
        length = len(s)
        zero_cnt += zero
        s = str(bin(length-zero))[2:]
        cnt += 1
    return [cnt, zero_cnt]
            
        