import numpy as np


def dist(pos1, pos2):
    return np.sqrt(np.sum((pos1-pos2)**2))


class Object:
    def __init__(self, canvas, m, r, p, v=np.array([0, 0]), f=np.array([0, 0], dtype=float)):
        self.mass=m
        self.radius=r
        self.position=p
        self.velocity=v
        self.force=f
        self.id=canvas.create_oval(np.round(self.position[0])-self.radius, np.round(self.position[1])-self.radius, np.round(self.position[0])+self.radius, np.round(self.position[1])+self.radius, fill="black")
    def interact(self, obj2):
        d=dist(self.position,obj2.position)
        F=float(self.mass*obj2.mass/(d**2))*10**3
        force_x=F*(obj2.position[0]-self.position[0])/d
        force_y=F*(obj2.position[1]-self.position[1])/d
        self.force+=np.array([force_x, force_y], dtype=float)
        obj2.force-=np.array([force_x, force_y], dtype=float)
    def move(self, canvas, dt):
        self.position+=self.velocity*dt
        canvas.move(self.id, np.round(self.velocity[0]*dt), np.round(self.velocity[1]*dt))
    def accelerate(self, dt):
        self.velocity+=self.force*dt/self.mass


