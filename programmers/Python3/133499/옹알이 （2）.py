def solution(babbling):
    can_speek = ["aya", "ye", "woo", "ma"]
    answer = 0
    for x in babbling:
        start = 0
        before_word = ""
        for end in range(1, len(x)+1):
            word = x[start:end]
            if word != before_word and word in can_speek:

                before_word = x[start:end]
                start = end
        if start == end: answer+=1
    return answer