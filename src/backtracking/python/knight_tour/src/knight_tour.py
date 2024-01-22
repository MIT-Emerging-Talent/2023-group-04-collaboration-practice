
#helper function
def isValid(a,b, n, chessBoard):
    """it checks the knight movement, is it in chessboard and is it a new spot or not"""
    if 0 <= a < n and 0<= b < n:
        if chessBoard[a][b] == -1:
            return True
    return False

#helper function
def knightSteps(n,totalMove,chessBoard,x,y,xMove, yMove):
    """It set the next movement"""
    # if totalMove == (n*n)+1:
    #     return True
    for j in range(8):
        nextX = x + xMove[j]
        nextY = y + yMove[j]
        if isValid(nextX, nextY, n, chessBoard):
            chessBoard[nextX][nextY] = totalMove
            if totalMove == (n*n):
                return True
            if knightSteps(n, totalMove+1, chessBoard, nextX, nextY, xMove, yMove):
               return True
            else:
               chessBoard[nextX][nextY] = -1
             
    return False  

         
    
        
def knight_tour(n):
    # creating our chess board(n*n)
    chessBoard = []
    for i in range(n):
        chessBoard.append([-1]*n)
    chessBoard[0][0] = 1
    totalMove =1
    #knight movement on chess
    xMove = [2, -2, -2, 2, 1, 1, -1, -1]
    yMove = [1, -1, 1, -1, 2, -2, 2, -2]
    if knightSteps(n,totalMove+1, chessBoard, 0,0, xMove,yMove):
        for i in chessBoard:
           print(i)

    else:
        return False
