from collections import Counter

def solution(message, spoiler_ranges):
    message = message + " "
    word_counts = Counter(message.split())
    
    word = ""
    flag = 0
    spoiler_index = 0
    for i in range(len(message)):
        c = message[i]
        if c == " ":
            if flag: word_counts[word] -= 1
            word = ""
            flag = 0
            continue
        word += c
        
        if spoiler_index<len(spoiler_ranges)-1 and spoiler_ranges[spoiler_index][1] < i: spoiler_index += 1
        if spoiler_ranges[spoiler_index][0] <= i <= spoiler_ranges[spoiler_index][1]:
            flag = 1
    return len(list(filter(lambda x: word_counts[x]==0, word_counts)))
