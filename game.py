import random
import math
import sys, pygame
from pygame.locals import *
import pygame.gfxdraw
 
WIDTH =  800
HEIGHT = 512
max_particles=600
centerx,centery=90,45
phantom_len=20
 
class Particle():
    def __init__(self):
        self.phantom=list()
        self.progreso=0
        self.x, self.y = (WIDTH/2)+(random.uniform(0.,1.)*50-random.uniform(0.,1.)*50-centerx),(HEIGHT/2)+(random.uniform(0.,1.)*50-random.uniform(0.,1.)*50-centery)
        self.w,self.h=WIDTH,HEIGHT
        a=random.randint(120,255)
        self.color = (a-random.randint(0,100),a-random.randint(0,50),a)
        self.radio = random.randint(1,3)
        self.varx1=random.uniform(0.,1.)*20
        self.varx2=random.uniform(0.,1.)*20
        self.vary1=random.uniform(0.,1.)*20
        self.vary2=random.uniform(0.,1.)*20
    

    def move(self,screen): 
        
        self.phantom.append((self.x,self.y))
        if len(self.phantom)>phantom_len:
            self.phantom.pop(0)
        count=0
        for x1,y1 in self.phantom:
            count+=1
            pygame.gfxdraw.filled_circle(screen,int(x1),int(y1),self.radio,(255,255,255,10))
        
        self.x = self.x + math.sin(self.progreso/self.varx1)*math.cos(self.progreso/self.varx2)
        self.y = self.y + math.sin(self.progreso/self.vary1)*math.cos(self.progreso/self.vary2)

        pygame.gfxdraw.filled_circle(screen,int(self.x),int(self.y),self.radio,self.color)
        self.progreso = self.progreso+1
        

def load_image(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error, message:
                raise SystemExit, message
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image
 
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("El chakra del kiwi")
 
    background_image = load_image('fondo2.jpg')
    bolas = [Particle() for i in xrange(max_particles)] 
    
    while True:
        
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
 
        screen.blit(background_image, (0, 0))
        for i in xrange(max_particles):
            bolas[i].move(screen)
            
        pygame.display.flip()
        
    return 0
 
if __name__ == '__main__':
    pygame.init()
    main()