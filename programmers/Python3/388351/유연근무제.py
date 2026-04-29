def solution(schedules, timelogs, startday):
    answer = len(schedules)
    for i in range(len(schedules)):
        today = startday-1
        schedules[i]+=10
        h, m = schedules[i]//100 + schedules[i]%100//60, schedules[i]%100%60
        for t in timelogs[i]:
            nh, nm = t//100, t%100
            if today < 5 and (nh>h or nh==h and nm>m):
                answer -= 1
                break
            today = (today+1)%7
    return answer