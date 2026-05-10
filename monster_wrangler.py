import pygame, random

#initialize pygame
pygame.init()

#set display window
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Monster Wrangler")


#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#main game loop
running = True
while running:
    #check to see if user quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #update display and clock
    pygame.display.update()
    clock.tick(FPS)

#end game
pygame.quit()