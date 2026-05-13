def solution(s):
    before = " "
    answer = ""
    for current in s:
        c = current
        if before == " " and "a"<=current<="z": c = chr(ord(current)-32)
        elif before != " " and "A"<=current<="Z": c = chr(ord(current)+32)
        answer += c
        before = c
    return answer