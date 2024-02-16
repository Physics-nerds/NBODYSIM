#importing essential modules
import pygame
import random
import numpy as np
import math
import matplotlib.pyplot as plt
#initaializing pygame constructer
pygame.init()

#some variables which are gomma be useful later on
screen_w = 800
screen_h = 600
window = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
running = True

#some contants
G = 6.673e-11

#creating class for creating bodies
class particle:
   
    
    def __init__(self,x_pos,y_pos,X_vel,y_vel,radius,color,mass):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_vel = X_vel
        self.y_vel = y_vel
        self.color = color
        self.radius = radius
        self.mass = mass
        self.angle = 90#random.uniform(0,2*math.pi)
    #function to draw the particles on screen
    def draw(self):
        pygame.draw.circle(window,self.color,(self.x_pos,self.y_pos),self.radius)

    def force(self,other):
        global ax,ay,f
        t = 60
        dx = (self.x_pos-other.x_pos)**2
        dy = (self.y_pos-other.y_pos)**2
        distance = math.sqrt(dx+dy)
        f = G*self.mass*other.mass/distance
        a = f/self.mass
        ax = a*math.cos(self.angle)
        ay = a*math.sin(self.angle)
 
    def values(ax,ay):
        return ax,ay


    #method to update the positions
    def update_pos(self):
        global x,v
        t = 60
        
        self.x_pos = self.x_vel+self.x_pos
        self.y_pos = self.y_vel+self.y_pos
        if self.x_pos<=0 or self.x_pos>=screen_w:
            self.angle = math.pi- self.angle
        if self.y_pos<=0 or self.y_pos>=screen_h:
            self.angle = math.pi-self.angle
        x = []
        v = []
        x.append(self.x_pos)
        v.append(self.x_vel)
    

    def force(self,other):
        global ax,ay,f
        t = 0.21
        dx = max((self.x_pos-other.x_pos)**2,1)
        dy = (self.y_pos-other.y_pos)**2
        distance = math.sqrt(dx+dy)
        f = G*self.mass*other.mass/distance
        a = f/self.mass
        ax = a*math.cos(math.atan(dy/dx))
        ay = a*math.sin(math.atan(dy/dx))
        self.x_vel = self.x_vel + ax*t
        self.y_vel = self.y_vel + ay*t
        


#creating entities
p1 = particle(100,50,0,0,20,"red",5)
p2 = particle(400,300,0,0,30,"yellow",10)

#function to calculate coordinates of barycenter
def center_mass(a,b):
    global x_cm,y_cm
    x_cm = ((a.x_pos*a.mass)+(b.x_pos*b.mass))/(a.mass+b.mass)
    y_cm = ((a.y_pos*a.mass)+(b.y_pos*b.mass))/(a.mass+b.mass)
    #print(x_cm,y_cm)






#defining the mainloop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running  = False
        p1.force(p2)
        p1.update_pos()
        """
        p1.x_vel += 0.05
        p1.y_vel += 0.05
        p2.x_vel += 0.01
        p2.y_vel += 0.03
        """
    window.fill("black")
    p1.draw()
    p2.draw()
    p1.force(p2)
    p1.update_pos()
    #p2.update_pos()
    
   
    """
    p1.x_pos = p1.x_pos + p1.x_vel
    p1.y_pos = p1.y_pos + p1.y_vel
    p2.x_pos = p2.x_pos + p2.x_vel
    p2.y_pos = p2.y_pos + p2.y_vel
    """
    pygame.display.flip()
    clock.tick(30)

