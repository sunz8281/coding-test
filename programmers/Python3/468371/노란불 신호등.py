def solution(signals):
    signals = signals[::-1]
    signals_len = len(signals)
    limit = 1
    for i in range(signals_len):
        limit *= sum(signals[i])
        
    time = 1
    sinhos = [0]*signals_len
    sinhos_cnt = [0]*signals_len
    while time < limit:
        
        time += 1
        for i in range(signals_len):
            sinhos_cnt[i] += 1
            if signals[i][sinhos[i]] == sinhos_cnt[i]:
                sinhos[i] = (sinhos[i]+1)%3
                sinhos_cnt[i] = 0
        
        for i in range(signals_len):
            if sinhos[i] != 1:
                break
        else: return time
    return -1
            
