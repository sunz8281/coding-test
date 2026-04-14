import sys
sys.setrecursionlimit(10000)

def dp(nodes):
    if not nodes: return [[], []]
    top_idx = 0
    for i in range(len(nodes)):
        if nodes[top_idx][1] < nodes[i][1]: top_idx = i
    left = dp(nodes[:top_idx])
    right = dp(nodes[top_idx+1:])
    return [[nodes[top_idx][2]] + left[0] + right[0], left[1] + right[1] + [nodes[top_idx][2]]]
    

def solution(nodeinfo):
    sorted_nodeinfo = sorted([(x, y, i+1) for i, (x, y) in enumerate(nodeinfo)], key=lambda x: x[0])
    return dp(sorted_nodeinfo)
    