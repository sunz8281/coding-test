def dfs(nexts, point, info, childrens):
    if point[0]>0 and point[0]<=point[1]: return point[0]
    mx = point[0]
    for next_node in nexts:
        new_point = [point[0], point[1]]
        new_point[info[next_node]] += 1
        new_nexts = [node for node in nexts if node != next_node] + childrens[next_node]
        mx = max(mx, dfs(new_nexts, new_point, info, childrens))
    return mx

def solution(info, edges):
    childrens = [[] for _ in range(len(info))]
    for p, c in edges:
        childrens[p].append(c)
    return dfs([0], [0, 0], info, childrens)