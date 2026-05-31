def solution(wallpaper):
    minx, miny = len(wallpaper), len(wallpaper[0])
    maxx, maxy = 0, 0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '.': continue
            minx, miny = min(minx, i), min(miny, j)
            maxx, maxy = max(maxx, i), max(maxy, j)
    answer = [minx, miny, maxx+1, maxy+1]
    return answer