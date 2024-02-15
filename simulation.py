#importing essential modules
import pygame
import random
import numpy as np
import math
from scipy.integrate import odeint

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
    
    def __init__(self,x_pos,y_pos,X_vel,y_vel,radius,color,mass):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_vel = X_vel
        self.y_vel = y_vel
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
        self.x_pos = self.x_vel*math.cos(self.angle)
        self.y_pos = self.y_vel*math.sin(self.angle)
        if self.x_pos<=0 or self.x_pos>=screen_w:
            self.angle = math.pi- self.angle
        if self.y_pos<=0 or self.y_pos>=screen_h:
            self.angle = math.pi-self.angle
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

    def force(self,other):
        x = (self.x_pos-other.x_pos)**2
        y = (self.y_pos-other.y_pos)**2
        r = max(math.sqrt(x+y),1)
        f  = self.mass*other.mass/r**2

        #acceleration component
        ax = f*x/r
        ay = f*y/r

        #updating particle velocity
        self.x_vel = ax/self.mass
        self.angle = math.atan(self.x_vel)
    """
    def return_dvdt():
        dvdt = F/self.mass
        return dvdt
    """



#creating entities
p1 = particle(50,50,0,0,20,"red",1)
p2 = particle(300,100,0,0,30,"yellow",10)

#function to calculate coordinates of barycenter
def center_mass(a,b):
    global x_cm,y_cm
    x_cm = ((a.x_pos*a.mass)+(b.x_pos*b.mass))/(a.mass+b.mass)
    y_cm = ((a.y_pos*a.mass)+(b.y_pos*b.mass))/(a.mass+b.mass)
    #print(x_cm,y_cm)

def return_dvdt(body_1):
    dvdt = F/body_1.mass
    return dvdt


#defining method for graviation
def grav(body_1,body_2):
    global r,F,acc
    #calculating distance between bodies
    
    
    r = math.sqrt(math.pow((body_1.x_pos-body_2.x_pos),2)+math.pow((body_1.y_pos-body_2.y_pos),2))
    np.vectorize()
    #defining the force
    F = G*body_1.mass*body_2.mass/math.pow(r,2)
    #dv = (F/m)dt
    #print(F)
    return F,r
def fvalue(f):
    return f
fvalue(grav(p1,p2))
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
        p1.x_vel += 0.05
        p1.y_vel += 0.05
        p2.x_vel += 0.01
        p2.y_vel += 0.03
        """
        if p1.x_pos >= screen_w:
            p1.x_vel -= 2
        elif p1.x_pos <= 0:
            p1.x_vel += 1
        """ 
    window.fill("black")
    p1.draw()
    p2.draw()
    p1.update_pos()
    p2.update_pos()
    center_mass(p1,p2)
    grav(p1,p2)
    """
    p1.x_pos = p1.x_pos + p1.x_vel
    p1.y_pos = p1.y_pos + p1.y_vel
    p2.x_pos = p2.x_pos + p2.x_vel
    p2.y_pos = p2.y_pos + p2.y_vel
    """
    pygame.display.flip()
    clock.tick(30)
