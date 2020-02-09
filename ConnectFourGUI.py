import pygame as pg
import sys
import ConnectFour as c4

SIZE = width, height = 640, 480
SCREEN = pg.display.set_mode(SIZE)

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

brd = None


def updateBoard(brd):
    for x in range(0, 6):
        for y in range(0, 7):
            pg.draw.rect(SCREEN, BLUE, (y * 80, x * 80, 80, 80))
            if brd[x][y] == ' ':
                pg.draw.circle(SCREEN, BLACK, (20 + (y * 80), 20 + (x * 80)), 30)
            if brd[x][y] == 'X':
                pg.draw.circle(SCREEN, RED, (20 + (y * 80), 20 + (x * 80)), 30)
            if brd[x][y] == 'O':
                pg.draw.circle(SCREEN, YELLOW, (20 + (y * 80), 20 + (x * 80)), 30)


def main():
    pg.init()
    brd = c4.defineBoard()
    turn = 'X'
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        updateBoard(brd)
        pg.display.update()
        while True:
            col = int(input('Select a column to drop your piece: '))
            if c4.checkCol(brd, col):
                c4.dropPiece(brd, col, turn)
                break
        if c4.checkWinner(brd, turn):
            break
        turn = c4.changeTurn(turn)


main()
