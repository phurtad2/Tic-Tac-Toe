#! ~/PycharmProjects/TicTacToe TicTacToeGUI.py
# ---------------------#
# A simple GUI for tic tac toe against an unbeatable program; user is automatically blue circle, while the "ai" is
# red crosses. The user is asked via terminal if he/she would like to go first, and thus the pygame window appears. This
# project was made specifically to test my own ability to understand the Minimax Algorithm, of which the computer uses
# to find it's most optimal move in the game.
# ---------------------#

__author__ = "Patrick Hurtado"
import pygame
import minimax

pygame.init()

running = True
playing = True

print("Do you want to go first? (y/n)")
circle = True if input() == 'y' else False
movefirst = not circle
first = 1
second = 2
height = 500
width = 500

black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
win = [[0] * 3 for _ in range(3)]

# Calculates all middle positions for all nine spaces
xch = height / 12
a = (int(width / 6), int(height / 6))
b = (int((3 * width) / 6), int(height / 6))
c = (int((5 * width) / 6), int(height / 6))

d = (int(width / 6), int((3 * height) / 6))
e = (int((3 * width) / 6), int((3 * height) / 6))
f = (int((5 * width) / 6), int((3 * height) / 6))

g = (int(width / 6), int((5 * height) / 6))
h = (int((3 * width) / 6), int((5 * height) / 6))
i = (int((5 * width) / 6), int((5 * height) / 6))

rad = int((height / 3) * .25)

# Instantiates Pygame Screen and TTT surface to place
screen = pygame.display.set_mode((width, height))
startScreen = pygame.Surface((100, 100))
tic = pygame.Surface((width, height))
startScreen.fill((170, 252, 163))

tic.fill((170, 252, 163))

# Draw's out board
pygame.draw.line(tic, black, (width / 3, 10), (1 * (width / 3), height - 10), 10)
pygame.draw.line(tic, black, ((2 * width) / 3, 10), (2 * (width / 3), height - 10), 10)
pygame.draw.line(tic, black, (10, (1 * width) / 3), (width - 10, (1 * width) / 3), 10)
pygame.draw.line(tic, black, (10, (2 * width) / 3), (width - 10, (2 * width) / 3), 10)

screen.blit(tic, (0, 0))

while running:
    screen.blit(tic, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             running = False

        if event.type == pygame.MOUSEBUTTONDOWN and playing:
            mouse = pygame.mouse.get_pos()
            if circle and playing:
                if width / 3 > mouse[0] > 0 and height / 3 > mouse[1] > 0 == win[0][0]:
                    pygame.draw.circle(tic, blue, a, rad, 7)
                    win[0][0] = first
                    circle = not circle
                    print("A")
                elif (2 * width) / 3 > mouse[0] > width / 3 and height / 3 > mouse[1] > 0 == win[1][0]:
                    pygame.draw.circle(tic, blue, b, rad, 7)
                    win[1][0] = first
                    circle = not circle
                    print("B")
                elif (3 * width) / 3 > mouse[0] > (2 * width) / 3 and height / 3 > mouse[1] > 0 == win[2][0]:
                    pygame.draw.circle(tic, blue, c, rad, 7)
                    circle = not circle
                    win[2][0] = first
                    print("C")
                elif (1 * width) / 3 > mouse[0] > 0 and (2 * height) / 3 > mouse[1] > height / 3 and 0 == win[0][1]:
                    pygame.draw.circle(tic, blue, d, rad, 7)
                    circle = not circle
                    win[0][1] = first
                    print("D")
                elif (2 * width) / 3 > mouse[0] > (1 * width) / 3 and (2 * height) / 3 > mouse[1] > height / 3 and 0 == \
                        win[1][1]:
                    pygame.draw.circle(tic, blue, e, rad, 7)
                    circle = not circle
                    win[1][1] = first
                    print("E")
                elif (3 * width) / 3 > mouse[0] > (2 * width) / 3 and (2 * height) / 3 > mouse[1] > height / 3 and 0 == \
                        win[2][1]:
                    pygame.draw.circle(tic, blue, f, rad, 7)
                    circle = not circle
                    win[2][1] = first
                    print("F")
                elif (1 * width) / 3 > mouse[0] > 0 and (3 * height) / 3 > mouse[1] > (2 * height) / 3 and 0 == win[0][
                    2]:
                    pygame.draw.circle(tic, blue, g, rad, 7)
                    circle = not circle
                    win[0][2] = first
                    print("G")
                elif (2 * width) / 3 > mouse[0] > (1 * width) / 3 and (3 * height) / 3 > mouse[1] > (
                            2 * height) / 3 and 0 == win[1][2]:
                    pygame.draw.circle(tic, blue, h, rad, 7)
                    circle = not circle
                    win[1][2] = first
                    print("H")
                elif (3 * width) / 3 > mouse[0] > (2 * width) / 3 and (3 * height) / 3 > mouse[1] > (
                            2 * height) / 3 and 0 == win[2][2]:
                    pygame.draw.circle(tic, blue, i, rad, 7)
                    circle = not circle
                    win[2][2] = first
                    print("I")
                if minimax.isGameOver(win) or minimax.isTie(win):
                    print("GAME OVER")
                    playing = False

    if not circle and playing:
        print("Xs Turn")
        win = list(minimax.minimax(list(win), movefirst))
        if win[0][0] == second:
            pygame.draw.line(tic, red, (a[0] - xch, a[1] - xch), (a[0] + xch, a[1] + xch), 7)
            pygame.draw.line(tic, red, (a[0] - xch, a[1] + xch), (a[0] + xch, a[1] - xch), 7)

            print("A")
        if win[1][0] == second:
            pygame.draw.line(tic, red, (b[0] - xch, b[1] - xch), (b[0] + xch, b[1] + xch), 7)
            pygame.draw.line(tic, red, (b[0] - xch, b[1] + xch), (b[0] + xch, b[1] - xch), 7)

            print("B")
        if win[2][0] == second:
            pygame.draw.line(tic, red, (c[0] - xch, c[1] - xch), (c[0] + xch, c[1] + xch), 7)
            pygame.draw.line(tic, red, (c[0] - xch, c[1] + xch), (c[0] + xch, c[1] - xch), 7)

            print("C")
        if win[0][1] == second:
            pygame.draw.line(tic, red, (d[0] - xch, d[1] - xch), (d[0] + xch, d[1] + xch), 7)
            pygame.draw.line(tic, red, (d[0] - xch, d[1] + xch), (d[0] + xch, d[1] - xch), 7)

            print("D")
        if win[1][1] == second:
            pygame.draw.line(tic, red, (e[0] - xch, e[1] - xch), (e[0] + xch, e[1] + xch), 7)
            pygame.draw.line(tic, red, (e[0] - xch, e[1] + xch), (e[0] + xch, e[1] - xch), 7)

            print("E")
        if win[2][1] == second:
            pygame.draw.line(tic, red, (f[0] - xch, f[1] - xch), (f[0] + xch, f[1] + xch), 7)
            pygame.draw.line(tic, red, (f[0] - xch, f[1] + xch), (f[0] + xch, f[1] - xch), 7)

            print("F")
        if win[0][2] == second:
            pygame.draw.line(tic, red, (g[0] - xch, g[1] - xch), (g[0] + xch, g[1] + xch), 7)
            pygame.draw.line(tic, red, (g[0] - xch, g[1] + xch), (g[0] + xch, g[1] - xch), 7)

            print("G")
        if win[1][2] == second:
            pygame.draw.line(tic, red, (h[0] - xch, h[1] - xch), (h[0] + xch, h[1] + xch), 7)
            pygame.draw.line(tic, red, (h[0] - xch, h[1] + xch), (h[0] + xch, h[1] - xch), 7)

            print("H")
        if win[2][2] == second:
            pygame.draw.line(tic, red, (i[0] - xch, i[1] - xch), (i[0] + xch, i[1] + xch), 7)
            pygame.draw.line(tic, red, (i[0] - xch, i[1] + xch), (i[0] + xch, i[1] - xch), 7)

            print("I")
        circle = not circle
        if minimax.isGameOver(win) or minimax.isTie(win):
            print("GAME OVER")
            playing = False

    pygame.display.update()
