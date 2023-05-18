import pygame
import random
import math

###
# All rights reserved for the images used in this game.
# Please find comment snippets in this code and the licenses included in the Licenses folder.
###


# Init pygame
pygame.init()

# Create window
screen = pygame.display.set_mode((900, 750))

# license-alien-planet-...
# Background
bg = pygame.image.load('Icons/bg_space.jpg')

# Title and Icon
pygame.display.set_caption("Space Guardians")
# Icon made from <a href="https://www.flaticon.com/free-icons/space-invaders" title="space invaders icons">Space invaders icons created by Freepik - Flaticon</a>
# Icon made from <a href="https://www.flaticon.com/free-icons/space-invaders" title="space invaders icons">Space invaders icons created by Smashicons - Flaticon</a>
ico = pygame.image.load('Icons/icon2.png')
pygame.display.set_icon(ico)

# Score
score_val = 0
font = pygame.font.Font('Fonts/Sunny Spells.ttf', 40)
txtX = 10
txtY = 10

# Game Over text
ovr_fnt = pygame.font.Font('Fonts/ka1.ttf', 70)


# Player Icon
playerIcon = pygame.image.load('Icons/spaceship.png')
playerX = 425
playerY = 650

# Enemies created by <a href="https://www.flaticon.com/free-icons/alien" title="alien icons">Alien icons created by Freepik - Flaticon</a>
# Enemy Icon
enemyIcon = []
enemyX = []
enemyY = []
enemyOC = []
enemyDWN = []
numEnemies = 6

for i in range(numEnemies):
    enemyIcon.append(pygame.image.load('Icons/enemy.png'))
    enemyX.append(random.randint(0, 834))
    enemyY.append(random.randint(50, 100))
    # Movement of enemy
    enemyOC.append(0.35)
    enemyDWN.append(25)

# license_bullet.pdf
# Bullet
bullIcon = pygame.image.load('Icons/bullet.png')
bulletX = 0
bulletY = playerY
bulletUP = 3
# Bullet states : Ready, Fired, TargetHit
# Ready - Ready to shoot; not visible to player
# Fired - Shots have been shot; visible to player
# TargetHit - Hit the enemy successfully; not visible to player - renders enemy invisible too!
bState = "Ready"



# Movement of ship
rateOC = 0

def showSc(x,y):
    score = font.render("Score : " + str(score_val), True, (255,255,255))
    screen.blit(score, (x, y))

def GO_txt():
    overText = ovr_fnt.render("GAME OVER!", True, (255,255,255), (0,0,0))
    screen.fill((0,0,0))
    screen.blit(overText, (225,200))
    global bState
    bState = "TargetHit"
    

def player(x,y):
    # Draw player
    screen.blit(playerIcon, (x, y))

def enemy(x,y,i):
    # Draw enemy
    screen.blit(enemyIcon[i], (x, y))

def fire_bull(x, y):
    # Fire the bullet when [SPACE] is pressed
    global bState
    bState = "Fired"
    screen.blit(bullIcon, (x+16, y+10)) # Draw bullet... Just in case you weren't looking at previous comments.

def isCollision(enemyX,enemyY,bulletX,bulletY):
    dist = math.sqrt(math.pow(enemyX-bulletX, 2) + math.pow(enemyY-bulletY, 2))
    if dist < 25:
        return True # Collision happened
    else:
        return False # Collision didn't happen

#def happyness(score,enemyX,enemyY,bulletY,bState):
#    score += 1
#    print(score)
#    bulletY = 650
#    bState = "Ready"
#    enemyX = random.randint(0, 834)
#    enemyY = random.randint(50, 100)

# Game Loop
proc = True
while proc:
    # Background
    screen.fill((200,0,105))
    # No more solid colours...
    screen.blit(bg, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            proc = False
        # Check keystroke isPressed :
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left arrow")
                rateOC = -0.5
                print(playerX)
            if event.key == pygame.K_RIGHT:
                print("Right arrow")
                rateOC = 0.5
                print(playerX)
            if event.key == pygame.K_SPACE:
                if bState is "Ready":
                    print("Shoot")
                    bulletX = playerX
                    fire_bull(bulletX, bulletY)
        # Check key release
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Key released")
                rateOC = 0
    playerX += rateOC
    # Boundaries
    if playerX <= 0:
        playerX = 0
    elif playerX >= 835:
        playerX = 835
    
    for i in range(numEnemies):
        #Game Over
        if enemyY[i] > 600:
            for j in range(numEnemies):
                enemyY[i] = 2000
            GO_txt()
            break

        enemyX[i] += enemyOC[i]
        if enemyX[i] <= 0:
            enemyOC[i] = 0.35
            enemyY[i] += enemyDWN[i]
        elif enemyX[i] >= 835:
            enemyOC[i] = -0.35
            enemyY[i] += enemyDWN[i]
        # Check for collision between bullet and alien
        col = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if col:
            #happyness(score, enemyX, enemyY, bulletY, bState)
            score_val += 1
            bulletY = 650
            bState = "Ready"
            enemyX[i] = random.randint(0, 834)
            enemyY[i] = random.randint(50, 100)
        enemy(enemyX[i], enemyY[i], i)
    
    # Bullet Movement
    if bulletY <= 0:
        bulletY = 650
        bState = "Ready"
    if bState is "Fired":
        fire_bull(bulletX, bulletY)
        bulletY -= bulletUP
    

    player(playerX,playerY)
    showSc(txtX,txtY)
    pygame.display.update()