import pygame
import time
import random
import webbrowser



pygame.init()

#Clock Stuff
clock = pygame.time.Clock()
fps = 60

#Defining Variables
right = False
left = False
roght = True
loft = False
win = False

#The cooldown variables
ecooldown = 1000
last_alien_shot = pygame.time.get_ticks()
movecooldown = 600
last_alien_move = pygame.time.get_ticks()
guncooldown = 500
last_plaser = pygame.time.get_ticks()
mom_cooldown = 10000
last_mom = pygame.time.get_ticks()
score = 0
text_font = pygame.font.SysFont("Comic Sans", 30)

#Screen Stuff
screen_width = 1000
screen_height = 750

#How many aliens spawn and how they spawn
rows = 6
collumn = 6

#Opening the music 
def music():
        moosic = "https://www.youtube.com/watch?v=k85mRPqvMbE"
        browser = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(browser)
        webbrowser.open(moosic)

music()
#Backround
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Invaders Space")

bg = pygame.image.load("invaders/img/space-bg2.png")
bg = pygame.transform.scale(bg, (1000, 750))

#Player Stuff
class PlayerShip(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("invaders/img/ship.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        

        global moveLeft
        global moveRight

        def moveRight(self, pixels):
            self.rect.x += pixels

        def moveLeft(self, pixels):
            self.rect.x -= pixels

#Writing the Text for score
def draw_text(text, font, text_col, x, y):
    ima = font.render(text, True, text_col)
    screen.blit(ima, (x,y))

#What the plaser properties are, sich as size
class pLaser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("invaders/img/laser.png")
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        

#What plaser does each tick
    def update(self):
        self.rect.y -= 20
        if self.rect.bottom < 0:
            self.kill()
        if pygame.sprite.spritecollide(self, alien_group, True):
            self.kill()
            global ecooldown
            global movecooldown
            global score
            ecooldown -= 20
            movecooldown -= 20
            score += 100

        if pygame.sprite.spritecollide(self, mom_group, True):
            self.kill()
            score += 500

#What q-bert's properties are, sich as size
class qBert(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("invaders/img/q-bert.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]


        
    def update(self):
        self.rect.x = random.randint(0, 1000)
        self.rect.y = random.randint(0, 750)

#What the mothership properties are, sich as size
class Mother_Ship(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("invaders/img/mom-ship.png")        
        self.image = pygame.transform.scale(self.image, (100, 50))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
            self.rect.x -= 2
            if self.rect.x == screen_width:
                self.kill()
                pass

#What the alien properties are, sich as size
class Alien(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("invaders/img/enemy" + str(random.randint(1,3)) + ".png")        
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

        self.move_counter = 0
        self.move_direction = 1
        self.direction = loft

    def update(self):
        
        for self in alien_group:
            if self.rect.x == 0:
                self.direction = roght
                self.rect.y += 35
                pass
            if self.rect.x + 49 == screen_width:
                self.direction = loft
                self.rect.y += 35
                pass

        for self in alien_group:
            if self.rect.y >= 700:
                self.kill()
                print("You lost the game")
                global running
                global win
                win = False
                running = False

        for self in alien_group:
            if self.direction == roght:
                self.rect.x += 1
            elif self.direction == loft:
                self.rect.x -= 1

#TYhe enemy Laser's base
class eLaser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("invaders/img/elaser.png")        
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]


#What elaser does each tick
    def update(self):
        self.rect.y += 5
        if self.rect.top < 0:
            self.kill()
        if pygame.sprite.spritecollide(self, playership_group, True):
            self.kill()
            print("Game Over")
            global running
            global win
            win = False
            running = False



#Grouping
playership_group = pygame.sprite.Group()
plaser_group = pygame.sprite.Group()
bert_group = pygame.sprite.Group()
alien_group = pygame.sprite.Group()
elaser_group = pygame.sprite.Group()
mom_group = pygame.sprite.Group()

#Spawn
playership = PlayerShip(int(screen_width / 2), screen_height - 40)
print(screen_width)
playership_group.add(playership)

#The spawning of the laiens
def creation():
    for row in range(rows):
        for item in range(collumn):
            arien = Alien(100 +(screen_width / collumn) + item * 100, 59 + row * 70)
            alien_group.add(arien)

creation()
#Putting the background on screen
def draw_bg():
    screen.blit(bg, (0, 0))


#The big game loop
running = True
while running:
    clock.tick(fps)
    draw_bg()


#Timers
##The elasers
    time_now = pygame.time.get_ticks()
    if time_now - last_alien_shot > ecooldown and len(alien_group) > 0:
        attacking_enemy = random.choice(alien_group.sprites())
        elaser = eLaser(attacking_enemy.rect.centerx, attacking_enemy.rect.bottom)
        elaser_group.add(elaser)
        last_alien_shot = time_now
##the alien movement
    time_nows = pygame.time.get_ticks()
    if time_nows - last_alien_move > movecooldown and len(alien_group) > 0:
        alien_group.update()
        last_alien_move = time_nows
##The mothership spawning cooldown
    Trime_now = pygame.time.get_ticks()
    if Trime_now - last_mom > mom_cooldown:
        mom_spawn = Mother_Ship(int(screen_width + 50), screen_height - 700) 
        mom_group.add(mom_spawn)
        last_mom = Trime_now
#How to exit a game via the x in the corner
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

#The movement/changes of everything
    plaser_group.update()
    bert_group.update()
    mom_group.update()
    elaser_group.update()

#Where the stuff is put on screen
    bert_group.draw(screen)
    mom_group.draw(screen)
    alien_group.draw(screen)
    playership_group.draw(screen)
    plaser_group.draw(screen)
    elaser_group.draw(screen)
    draw_text("Score: " + str(score), text_font, (255, 255, 255), 50, 50)
    keys = pygame.key.get_pressed()

    #Player Movement
    if keys[pygame.K_LEFT] and playership.rect.left > 0:
        moveLeft(playership, 5)       

    if keys[pygame.K_RIGHT] and playership.rect.right < 1000:
        moveRight(playership, 5)

    if keys[pygame.K_SPACE] or keys[pygame.K_1]:
        time_currently = pygame.time.get_ticks()
        if time_currently - last_plaser > guncooldown:
            glaser = pLaser(playership.rect.centerx, playership.rect.centery)
            plaser_group.add(glaser)        
            last_plaser = time_currently

#####Where the code to q-bert's movement and creation lie
#        bert_spawn = qBert(int(screen_width / 2 + 50), screen_height - 50) 
#        bert_group.add(bert_spawn)

#Q-bert Movement
#    right = True
#    left = False
#    for bert_spawn in bert_group:
#        if right:
#            bert_spawn.rect.x -= 10
#
#        elif left:
#            bert_spawn.rect.x += 10
#
#        elif bert_spawn.rect.right > 1750:
#            bert_spawn.rect.y += 50
#            left = True
#            right = False
#        
#        elif bert_spawn.rect.right < 0:
#            bert_spawn.rect.y -= 50
#            right = True
#            left = False

    if len(alien_group) <= 0:
        print("YOU WON THE GAME, I GUESS")
        win = True
        running = False
    
    print(movecooldown)


    pygame.display.update()
#Win/loss display
if win == False:
    draw_text("You have FAILED", text_font, (255, 255, 255), screen_width / 2, screen_height / 2)
    pygame.display.update()
if win == True:
    draw_text("You've won, I guess", text_font, (255, 255, 255), screen_width / 2, screen_height / 2)
    pygame.display.update()

time.sleep(3)

pygame.quit()