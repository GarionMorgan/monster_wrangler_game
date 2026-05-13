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

#Define Classes
class Game():
    """A class to control game play"""
    def __init__(self):
        """Initialize game object"""
        pass

    def update(self):
        """update game object"""
        pass

    def draw(self):
        """draw objects to display"""
        pass

    def check_collisions(self):
        """check for collisions between player and monsters"""
        pass

    def start_new_round(self):
        """populate board with new monsters"""
        pass

    def choose_new_target(self):
        """choose new target for player"""
        pass

    def pause_game(self):
        """pause game"""
        pass

    def reset_game(self):
        """reset game"""
        pass

class Player(pygame.sprite.Sprite):
    """player class that user can control"""
    def __init__(self):
        """initialize player"""
        pass

    def update(self):
        """update player"""
        pass

    def warp(self):
        """warp player to safe zone"""
        pass

    def reset(self):
        """resets player position"""
        pass

class Monster(pygame.sprite.Sprite):
    """class to create enemy objects"""
    def __init__(self):
        """initialize monster"""
        pass

    def update(self):
        """update monster"""
        pass

#create a player group and object
my_player_group = pygame.sprite.Group()
my_player = Player()
my_player_group.add(my_player)

#create monster group
my_monster_group = pygame.sprite.Group()

#crate game object
my_game = Game()


#main game loop
running = True
while running:
    #check to see if user quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #fill display
    display_surface.fill((0,0,0))

    #update and draw sprite groups
    my_player_group.update()
    my_player_group.draw(display_surface)

    my_monster_group.update()
    my_monster_group.draw(display_surface)

    #update and draw game
    my_game.update()
    my_game.draw()

    #update display and clock
    pygame.display.update()
    clock.tick(FPS)

#end game
pygame.quit()