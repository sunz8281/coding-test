def solution(video_len, pos, op_start, op_end, commands):
    trans = {"next": 10, "prev": -10}
    current = pos
    for command in commands:
        if op_start<=current<op_end:
            current = op_end
        m, s = map(int, current.split(':'))
        s += trans[command]
        m, s = m+s//60, s%60
        current = f"{m:02d}:{s:02d}"
        
        if current<"00:00": current = "00:00"
        if current>video_len: current = video_len
    if op_start<=current<op_end:
        current = op_end
    return current