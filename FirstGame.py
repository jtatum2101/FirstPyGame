import os
import sys

import pygame
from pygame import key

pygame.init()

window = pygame.display.set_mode((500,480))

pygame.display.set_caption('First Pygame')

walkRight = [pygame.image.load('tile000.png'), pygame.image.load('tile001.png'), pygame.image.load('tile002.png'), pygame.image.load('tile003.png'), pygame.image.load('tile004.png'), pygame.image.load('tile005.png'), pygame.image.load('tile006.png'), pygame.image.load('tile007.png'), pygame.image.load('tile008.png'), pygame.image.load('tile009.png'), pygame.image.load('tile010.png'), pygame.image.load('tile011.png'), pygame.image.load('tile012.png'), pygame.image.load('tile013.png'), pygame.image.load('tile014.png'), pygame.image.load('tile015.png'), pygame.image.load('tile016.png'), pygame.image.load('tile017.png'), pygame.image.load('tile018.png'), pygame.image.load('tile019.png'), pygame.image.load('tile020.png'), pygame.image.load('tile021.png'), pygame.image.load('tile022.png'), pygame.image.load('tile023.png'), pygame.image.load('tile024.png'), pygame.image.load('tile025.png'), pygame.image.load('tile026.png')]
walkLeft = [pygame.image.load('tile000-left.png'), pygame.image.load('tile001-left.png'), pygame.image.load('tile002-left.png'), pygame.image.load('tile003-left.png'), pygame.image.load('tile004-left.png'), pygame.image.load('tile005-left.png'), pygame.image.load('tile006-left.png'), pygame.image.load('tile007-left.png'), pygame.image.load('tile008-left.png'), pygame.image.load('tile009-left.png'), pygame.image.load('tile010-left.png'), pygame.image.load('tile011-left.png'), pygame.image.load('tile012-left.png'), pygame.image.load('tile013-left.png'), pygame.image.load('tile014-left.png'), pygame.image.load('tile015-left.png'), pygame.image.load('tile016-left.png'), pygame.image.load('tile017-left.png'), pygame.image.load('tile018-left.png'), pygame.image.load('tile019-left.png'), pygame.image.load('tile020-left.png'), pygame.image.load('tile021-left.png'), pygame.image.load('tile022-left.png'), pygame.image.load('tile023-left.png'), pygame.image.load('tile024-left.png'), pygame.image.load('tile025-left.png'), pygame.image.load('tile026-left.png')]
bg = pygame.image.load('make-backgrounds-for-games.jpg')
char = pygame.image.load('tile000.png')

x = 50

y = 400

width = 40

height = 60

vel = 5

run = True

isJump = False 

left = False

right = False

walkCount = 0

clock = pygame.time.Clock()

jumpCount = 10

def redrawGameWindow():
    global walkCount
    
    window.blit(bg, (0,0))  
    if walkCount + 1 >= 27:
        walkCount = 0
        pygame.display.update()
        
    if left:  
        window.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1 
                                 
    elif right:
        window.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
        
    else:
        window.blit(char, (x, y))
        walkCount = 0
      
    
    pygame.display.update()


run = True

while run:
    clock.tick(45)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > vel: 
        x -= vel
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < 500 - vel - width:  
        x += vel
        left = False
        right = True
        
    else: 
        left = False
        right = False
        walkCount = 0
        
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False

    redrawGameWindow() 
    
    
pygame.quit()