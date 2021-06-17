import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import sys, pygame
from pygame.locals import *
pygame.init()

speed = [60, 60]
color = (255, 250, 250)
width = 550
height = 300

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame bouncing ball")

ball = pygame.image.load("eightball.jfif")
rect_boundry = ball.get_rect()

while 1:
    for event in pygame.event.get():
        rect_boundry = rect_boundry.move(speed)
        if rect_boundry.left < 0 or rect_boundry.right > width:
            speed[0] = -speed[0]
        if rect_boundry.top < 0 or rect_boundry.bottom > height:
            speed[1] = -speed[1]

        screen.fill(color)
        screen.blit(ball, rect_boundry)
        pygame.display.flip()

        if event.type == QUIT:
            pygame.quit()
            sys.exit()