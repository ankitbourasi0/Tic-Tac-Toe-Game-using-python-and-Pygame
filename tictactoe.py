import pygame as pg, sys

from pygame import gfxdraw
import numpy as np
pg.init()

#CONSTANTS-----------------------------------------------------
SCREEN_WIDTH = 900
SCREEN_HEIGHT = SCREEN_WIDTH
BG_COLOR = (28,170,156)
LINE_COLOR = (23,145,135)
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLUMN = 3
CIRCLE_WIDTH = 10
CROSS_WIDTH = 20
CIRCLE_COLOR = (239,231,200)
CROSS_COLOR = (66,66,66)
SQUARE_SIZE = SCREEN_WIDTH // BOARD_COLUMN
SPACE = SQUARE_SIZE // 4
CIRCLE_RADIUS = SQUARE_SIZE // 3

GameScreen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pg.display.set_caption('TIC TAC TOE')
GameScreen.fill(BG_COLOR)

#Game Board
board = np.zeros((BOARD_ROWS,BOARD_COLUMN))


def DrawLines():
    #1 horizontal line
    pg.draw.line(GameScreen,LINE_COLOR,(50,SQUARE_SIZE),(SCREEN_WIDTH-50,SQUARE_SIZE),LINE_WIDTH)
    #2 horizontal line
    pg.draw.line(GameScreen,LINE_COLOR,(50,2* SQUARE_SIZE),(SCREEN_WIDTH-50,2* SQUARE_SIZE),LINE_WIDTH)
    
    #1 Vertical line
    pg.draw.line(GameScreen,LINE_COLOR,(SQUARE_SIZE,50),(SQUARE_SIZE,SCREEN_HEIGHT-50),LINE_WIDTH)
    #2 Vertical line
    pg.draw.line(GameScreen,LINE_COLOR,(2* SQUARE_SIZE,50),(2* SQUARE_SIZE,SCREEN_HEIGHT-50),LINE_WIDTH)

def DrawFigures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLUMN):
            if board[row][col] == 1:
                gfxdraw.aacircle(GameScreen,int(col*SQUARE_SIZE +SQUARE_SIZE //2 ),int(row * SQUARE_SIZE + SQUARE_SIZE //2 ),CIRCLE_RADIUS,CIRCLE_COLOR)
                pg.draw.circle(GameScreen, CIRCLE_COLOR,(int(col * SQUARE_SIZE + SQUARE_SIZE //2  ),int(row * SQUARE_SIZE + SQUARE_SIZE //2 )),CIRCLE_RADIUS,10)
                gfxdraw.aacircle(GameScreen,int(col*SQUARE_SIZE +SQUARE_SIZE //2 ),int(row * SQUARE_SIZE + SQUARE_SIZE //2 ),CIRCLE_RADIUS-10,CIRCLE_COLOR)
            elif board[row][col] == 2:
                pg.draw.line(GameScreen,CROSS_COLOR,(col * SQUARE_SIZE + SPACE,row *SQUARE_SIZE +SQUARE_SIZE - SPACE),(col * SQUARE_SIZE + SQUARE_SIZE -SPACE,row * SQUARE_SIZE +SPACE),CROSS_WIDTH)
                pg.draw.line(GameScreen,CROSS_COLOR,(col * SQUARE_SIZE + SPACE,row *SQUARE_SIZE +SPACE),(col * SQUARE_SIZE + SQUARE_SIZE -SPACE,row * SQUARE_SIZE +SQUARE_SIZE - SPACE),CROSS_WIDTH)
 

def MarkSqaures(rows,cols,player):
    board[rows][cols] = player
def AvailableSquares(rows,cols):
    return board[rows][cols] == 0
    #if correct return true else false 

#check is first square available?
    # print(AvailableSquares(0,0))
#now mark the first square then check-
    # MarkSqaures(0,0,1)
# print(AvailableSquares(0,0))

#Checking is board full 
def IsBoardFull():
    for row in range(BOARD_ROWS):
        for col in  range(BOARD_COLUMN):
            if board[row][col] ==0:
                return False
    return True

#Checking after marking full board
     # for row in range(BOARD_ROWS):
     #     for col in range(BOARD_COLUMN):
     #         MarkSqaures(row,col,1)
     # print(IsBoardFull())
# print(board)

 
def CheckWin(player):
    #Vertical win Check
    for col in range(BOARD_COLUMN):
        if board[0][col] == player and board[1][col] ==player and board[2][col] == player:
            DrawVerticalWinningLines(col,player) 
            return True
    
    #Horizontal win Check
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            DrawHorizontalWinningLines(row,player)
            return True
        
    #Right Diagonal win Check
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        DrawRightDiagonal(player)
        return True

    #Left Diagonal win Check
    if board[0,2] == player and board[1][1] == player and board[2][0] == player:
        DrawLeftDiagonal(player)
        return True
    
    return False
def DrawVerticalWinningLines(col,player):
    posX = col * SQUARE_SIZE + SQUARE_SIZE //2
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    pg.draw.line(GameScreen,color,(posX,15),(posX,SCREEN_HEIGHT -15),LINE_WIDTH)

def DrawHorizontalWinningLines(row,player):
    posY = row * SQUARE_SIZE + SQUARE_SIZE //2
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    pg.draw.line(GameScreen,color,(15,posY),(SCREEN_WIDTH - 15,posY),LINE_WIDTH)
def DrawRightDiagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    pg.draw.line(GameScreen,color,(15,15),(SCREEN_WIDTH - 15,SCREEN_HEIGHT-15),LINE_WIDTH)
def DrawLeftDiagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    pg.draw.line(GameScreen,color,(SCREEN_WIDTH-15,15),(15,SCREEN_HEIGHT-15),LINE_WIDTH)
def RestartGame():
    GameScreen.fill(BG_COLOR)
    DrawLines()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLUMN):
            board[row][col] = 0

DrawLines()
#GAME LOOP-----------------------------------------------------
player = 1  
game_over = False
while True:
 
    for e in pg.event.get():
        if e.type == pg.QUIT:
            sys.exit()
        if e.type == pg.MOUSEBUTTONDOWN and not game_over:
            mouseX = e.pos[0] #x
            mouseY = e.pos[1] #y
            
            clicked_row = int(mouseY // SQUARE_SIZE  )
            clicked_col = int(mouseX // SQUARE_SIZE  )

            # print(mouseX)
            # print(mouseY)
            print(clicked_row)
            print(clicked_col)
            if AvailableSquares(clicked_row,clicked_col):
                #Optimized 
                MarkSqaures(clicked_row,clicked_col,player)
                if CheckWin(player):
                    game_over =True
                player = player % 2 +1 
                #Old 
                # if player == 1:
                    # MarkSqaures(clicked_row,clicked_col,player)
                #     if CheckWin(player):
                #         game_over = True
                #     player = 2
                # elif player == 2:
                #     MarkSqaures(clicked_row,clicked_col,player)
                #     if CheckWin(player):
                #         game_over = True
                #     player = 1

                DrawFigures()
                # print(board)

        if e.type == pg.KEYDOWN:
            if e.key == pg.K_r:
                RestartGame()
                game_over =  False

    
    
    pg.display.update()
