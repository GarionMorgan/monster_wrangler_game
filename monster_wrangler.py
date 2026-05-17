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
        super().__init__()
        self.image = pygame.image.load("./monster_wrangler_assets/knight.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = WINDOW_WIDTH//2
        self.rect.bottom = WINDOW_HEIGHT

        self.lives = 5
        self.warps = 2
        self.velocity = 8

        self.catch_sound = pygame.mixer.Sound("./monster_wrangler_assets/catch.wav")
        self.die_sound = pygame.mixer.Sound("./monster_wrangler_assets/die.wav")
        self.warp_sound = pygame.mixer.Sound("./monster_wrangler_assets/warp.wav")

    def update(self):
        """update player"""
        keys = pygame.key.get_pressed()

        #move player within the bounds of the screen
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            self.rect.x += self.velocity
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.velocity
        if keys[pygame.K_DOWN] and self.rect.bottom < WINDOW_HEIGHT:
            self.rect.y += self.velocity

    def warp(self):
        """warp player to safe zone"""
        if self.warps > 0:
            self.warps -= 1
            self.warp_sound.play()
            self.rect.bottom = WINDOW_HEIGHT

    def reset(self):
        """resets player position"""
        self.rect.centerx = WINDOW_WIDTH//2
        self.rect.bottom = WINDOW_HEIGHT

class Monster(pygame.sprite.Sprite):
    """class to create enemy objects"""
    def __init__(self, x, y, image, monster_type):
        """initialize monster"""
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

        #monster type is an int 0 -> blue, 1-> green, 2 -> purple, 3 -> yellow
        self.type = monster_type

        #set random motion
        self.dx = random.choice([-1,1])
        self.dy = random.choice([-1,1])
        self.velocity = random.randint(1,5)

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