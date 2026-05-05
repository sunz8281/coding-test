def solution(n, w, num):
    row = (num-1)//w+1
    if row%2: col=(num-1)%w+1
    else: col=w-(num-1)%w
    
    over = (n-1)%w+1
    box_height = (n-1)//w+1
    if box_height%2:
        box = box_height - int(over<col)
    else:
        box = box_height - int(w-over>=col)
    print(col, row, box, box_height)
    return box - row + 1