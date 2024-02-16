#importing essential modules
import pygame
import random
import numpy as np
import math
from scipy.integrate import odeint
import pymunk

#initaializing pygame constructer
pygame.init()

#some variables which are gomma be useful later on
screen_w = 800
screen_h = 600
window = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
running = True

#some contants
G = 6.673 * math.pow(10,-11)

#creating class for creating bodies
class particle:
    x = []
    y = []
    
    def __init__(self,x_pos,y_pos,vel,radius,color,mass):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.vel = vel
        self.color = color
        self.radius = radius
        self.mass = mass
        self.angle = random.uniform(0,2*math.pi)

    #function to draw the particles on screen
    def draw(self):
        pygame.draw.circle(window,self.color,(self.x_pos,self.y_pos),self.radius)

    #method to update the positions
    def update_pos(self):
        global t
        self.x_pos += self.vel*math.cos(self.angle)
        self.y_pos += self.vel*math.sin(self.angle)
        if self.x_pos<=0 or self.x_pos>=screen_w:
            self.angle = math.pi-self.angle
        if self.y_pos<=0 or self.y_pos>=screen_h:
            self.angle = 2*math.pi-self.angle
        """    
        t = np.linspace(0,10)
        acc = F/self.mass
        #x_vel = odeint(return_dvdt,self.x_vel,t)
        #self.x_pos = self.x_pos + self.x_vel
        #self.y_pos = self.y_pos + self.y_vel
        self.x_pos = self.x_pos + (acc*t)
        self.y_pos = self.y_pos + (acc*t)
        """

    def center_r(self):
        self.x_pos*self.mass/self.mass
        pass
    #defining acceleration
    
    def force(self,other):
        global r
        dx = (self.x_pos-other.x_pos)**2
        dy = (self.y_pos-other.y_pos)**2
        r = max(math.sqrt(dx+dy),1)
        f  = self.mass*other.mass/10e5
        ax = f*dx/r
        ay = f*dy/r
        #updating particle velocity
        self.vel += ax/self.mass
        self.angle = math.atan2(self.vel*math.sin(self.angle)+ay/self.mass,self.vel*math.cos(self.angle)+ax/self.mass)

    def collision(self,other):
            if r <= self.radius+other.radius:
                self.angle = (math.pi)/2-self.angle
            #acceleration component



#creating entities
p1 = particle(50,5,random.randint(1,5),5,"red",0.2)
p2 = particle(400,300,random.randint(1,5),20,"light blue",2)
p3 = particle(100,500,random.randint(1,5),5,"red",0.21)
#function to calculate coordinates of barycenter
def center_mass(a,b):
    global x_cm,y_cm
    x_cm = ((a.x_pos*a.mass)+(b.x_pos*b.mass))/(a.mass+b.mass)
    y_cm = ((a.y_pos*a.mass)+(b.y_pos*b.mass))/(a.mass+b.mass)
    return x_cm,y_cm
    #print(x_cm,y_cm)



#defining the mainloop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running  = False
        """
        p1.x_vel += 0.05
        p1.y_vel += 0.05
        p2.x_vel += 0.01
        p2.y_vel += 0.03
        """
       
        """
        if p1.x_pos >= screen_w:
            p1.x_vel -= 2
        elif p1.x_pos <= 0:
            p1.x_vel += 1
        """ 

    window.fill("black")
    p1.draw()
    p2.draw()
    p3.draw()
    p1.force(p2)
    
    p2.force(p1)
    p3.force(p1)
    p1.collision(p2)
    p3.collision(p1)
    p2.collision(p3)
    p1.update_pos()
    p2.update_pos()
    p3.update_pos()
    center_mass(p1,p2)
    
    """
    p1.x_pos = p1.x_pos + p1.x_vel
    p1.y_pos = p1.y_pos + p1.y_vel
    p2.x_pos = p2.x_pos + p2.x_vel
    p2.y_pos = p2.y_pos + p2.y_vel
    """
    pygame.display.set_caption("Two Body Simulation")
    pygame.display.flip()
    clock.tick(30)



