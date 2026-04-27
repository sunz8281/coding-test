def solution(bandage, health, attacks):
    t, x, y = bandage
    l_t = 0
    current = health
    for attack in attacks:
        a_t, a_p = attack
        cnt = a_t - l_t - 1
        current = min(current + cnt*x + (cnt//t)*y, health) - a_p
        l_t = a_t
        if current<=0: return -1
    return current