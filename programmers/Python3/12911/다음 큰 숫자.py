def solution(n):
    x = str(bin(n))[2:]
    one_cnt = 0
    length = len(x)
    before = "0"
    for i in range(1, length+1):
        if x[-i]=="0" and before=="1":
            break
        if x[-i]=="1": one_cnt+=1
        before = x[-i]
    else: i+=1
    result = x[:-i] + "1" + "0"*(i-one_cnt) + "1"*(one_cnt-1)
    return int(result, 2)