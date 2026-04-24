def solution(board, h, w):
    return [board[x][y] == board[h][w] for x, y in ((h, w+1), (h, w-1), (h-1, w), (h+1, w)) if 0<=x<len(board) and 0<=y<len(board[0])].count(True)