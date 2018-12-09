import Objects
import numpy as np
from tkinter import *
from Setup import *


stop=False


def collision(a, b):
    return a.radius+b.radius>=Objects.dist(a.position, b.position)


def update_field():
    global stop
    global root
    global canvas
    global dt
    global F
    global a
    for i in range(len(a)):
        a[i].move(canvas, dt)
        a[i].accelerate(dt)
        a[i].force=np.array(F, dtype=float)
    i=0
    while i<len(a):
        j=i+1
        while j<len(a):
            if collision(a[i], a[j]):
                a[i].velocity=(a[i].mass*a[i].velocity+a[j].mass*a[j].velocity)/(a[i].mass+a[j].mass)
                a[i].mass+=a[j].mass
                a[i].radius=np.round((a[i].radius**3+a[j].radius**3)**(1./3))
                a[i].position+=a[j].position
                a[i].position/=2
                canvas.delete(a[j].id)
                del a[j]
                break
            a[i].interact(a[j])
            j+=1
        i+=1
    if not stop:
        root.after(100, update_field)

def start(_root, _canvas, setup, _dt):
    global stop
    global root
    global canvas
    global dt
    global F
    global a
    stop=False
    root=_root
    canvas=_canvas
    a=setup.a
    dt=_dt
    F=setup.F
    def stop_command():
        global stop
        stop=not stop
        if stop:
            btn.config(text="Start")
            setup_btn.config(state=NORMAL)
        else:
            btn.config(text="Pause")
            setup_btn.config(state=DISABLED)
            update_field()
    def setup_command():
        _canvas.config(state=DISABLED)
        setup=Setup(_root, _canvas)
        _canvas.config(state=NORMAL)
        btn.destroy()
        setup_btn.destroy()
        for i in a:
            _canvas.delete(i.id)
        start(_root, _canvas, setup, _dt)
    btn=Button(_root, text="Pause", command=stop_command)
    btn.pack(side="right")
    setup_btn=Button(_root, text="Setup", state=DISABLED, command=setup_command)
    setup_btn.pack(side="left")
    update_field()