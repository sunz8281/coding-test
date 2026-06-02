def solution(s, skip, index):
    answer = ''
    for c in s:
        x = ord(c) - 97
        for i in range(index):
            while True: 
                x = (x+1)%26
                if chr(x+97) not in skip: break
        answer += chr(x+97)
    return answer