
# n queens problem

def isSafe(board,row,col):
    for r in range(len(board)):
        if r != row and board[r][col] == 1:
            return False

    for c in range(len(board[0])):
        if c != col and board[row][c] == 1:
            return False

    r,c = row-1,col-1
    while r>=0 and c>=0:
        if board[r][c] == 1:
            return False
        r -= 1
        c -= 1

    r,c = row-1,col+1
    while r>=0 and c<len(board[0]):
        if board[r][c] == 1:
            return False
        r -= 1
        c += 1
 
    return True

def helper(board,row):
    if row == len(board):
        for idx in range(len(board)):
            print(board[idx])
        print('')
        return

    for col in range(len(board[0])):
        if isSafe(board,row,col):
            board[row][col] = 1
            helper(board,row+1)
            board[row][col] = 0

def solution(n):
    board = [ [0 for x in range(n)] for y in range(n)]
    helper(board,0)

def main():
    n = 4
    solution(n)

if __name__ == "__main__":
    main()

