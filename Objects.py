import numpy as np
import tkinter


def dist(pos1, pos2):
    return np.sqrt((pos1[0]-pos2[0])**2+(pos1[1]-pos2[1])**2)


class Object:
    def __init__(self, m, r, p, v=np.array([0, 0]), f=np.array([0, 0])):
        self.mass=m
        self.radius=r
        self.position=p
        self.velocity=v
        self.force=f
    def interact(self, obj2):
        d=dist(self.position,obj2.position)
        F=self.mass*obj2.mass/(d**2)
        force=F*(obj2.position-self.position)/d
        self.force+=force
        obj2.force-=force
    def move(self, dt):
        self.position+=self.velocity*dt
    def accelerate(self, dt):
        self.velocity+=self.force*dt/self.mass
    def draw(self, canvas, color):
        canvas.create_oval(self.position[0]-self.radius, self.position[1]-self.radius, self.position[0]+self.radius, self.position[1]+self.radius, fill=color)


