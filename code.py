
import pygame
pygame.init()

window=pygame.display.set_mode((500,1000))
pygame.display.set_caption('first game')
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
background = pygame.image.load('background.png')
char = pygame.image.load('standing.png')

clock=pygame.time.Clock()

class player:
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=10
        self.isJump=False
        self.jumpCount=10
        self.left=False
        self.right=False
        self.walkCount=0

    def draw(self,window):
        if self.walkCount +1>=27:
            self.walkCount=0
            
        if self.left:
            window.blit(walkLeft[self.walkCount//3],(self.x,self.y))
            self.walkCount +=1
        elif self.right:
            window.blit(walkRight[self.walkCount//3],(self.x,self.y))
            self.walkCount +=1
        else:
            window.blit(char,(self.x,self.y))


def redrawGameWindow():
    window.blit(background,(0,0))
    man.draw(window)

    pygame.display.update()



#main loop
man=player(300,204,64,64)
run = True
while run:
    clock.tick(27)
        
    redrawGameWindow()
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    keys=pygame.key.get_pressed()


##    if x>500:
##        x=0
##    if y>500:
##        y=0
##    if y<0:
##        y=499
##    if x<0:
##        x=499
        
    if keys[pygame.K_LEFT] and man.x>=man.vel:
            man.x-=man.vel
            man.left=True
            man.right=False
        
    elif keys[pygame.K_RIGHT] and man.x<500-50:
            man.x+=man.vel
            man.right=True
            man.left=False
    else:
        man.right=False
        man.left=False
        man.walkCount=0
            
    if not(man.isJump):
        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.right=False
            man.left=False
            man.walkCount=0
    else:
        if man.jumpCount >=-10:
            neg=1
            if man.jumpCount<0:
                neg = -1
            man.y -= (man.jumpCount**2)*0.25 * neg 
            man.jumpCount-=1
        else:
            man.isJump = False
            man.jumpCount=10
            
            
pygame.quit()
