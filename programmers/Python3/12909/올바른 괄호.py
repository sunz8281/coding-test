def solution(s):
    gualho = 0
    for c in s:
        if c == "(": gualho+=1
        else:
            if not gualho: return False
            gualho-=1
        
    if gualho: return False
    return True