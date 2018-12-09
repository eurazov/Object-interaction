from tkinter import *
import numpy as np
import Objects
n=2
#wait=IntVar()


class Setup:
    def __init__(self, root, canvas):
        global n
        global wait
        self.F=initial(root)
        self.n=n
        self.a=object_list(root, canvas)


class param:
    def __init__(self, w, i):
        self.m =Entry(w, width=10)
        self.m.grid(row=i+1, column=1)
        self.x =Entry(w, width=10)
        self.x.grid(row=i+1, column=2)
        self.y =Entry(w, width=10)
        self.y.grid(row=i+1, column=3)
        self.Vx=Entry(w, width=10)
        self.Vx.insert(0, '0')
        self.Vx.grid(row=i+1, column=4)
        self.Vy=Entry(w, width=10)
        self.Vy.insert(0, '0')
        self.Vy.grid(row=i+1, column=5)
        self.r =Entry(w, width=10)
        self.r.insert(0, '5')
        self.r.grid(row=i+1, column=6)


def initial(root):
    def get_amount():
        global n
        n = int(entry_amount.get())
        F[0]=float(entry_x.get())
        F[1]=float(entry_y.get())
        #destroy the fields
        w.destroy()
        #wait=False
    F=np.array([0, 0], dtype=float)
    w=Frame(root)
    w.pack()
    label_set_amount = Label(w, text="Choose the amount of objects.")
    label_set_amount.pack()
    entry_amount = Entry(w)
    entry_amount.focus_set()
    entry_amount.insert(0, str(n))
    entry_amount.pack()
    okbutton=Button(w, text="OK", command=get_amount)
    okbutton.pack()
    label_set_force=Label(w, text="Enter the constant force value.")
    label_set_force.pack()
    label_x=Label(w, text="x")
    label_x.pack(side="left")
    label_y=Label(w, text="y")
    label_y.pack(side="right")
    entry_x=Entry(w)
    entry_x.insert(0, '0')
    entry_x.pack(side="left")
    entry_y=Entry(w)
    entry_y.insert(0, '0')
    entry_y.pack(side="left")
    w.wait_window()
    return F


def object_list(root, canvas):
    def get_param():
        for i in entries:
            a.append(Objects.Object(canvas, float(i.m.get()), float(i.r.get()), np.array([float(i.x.get()), float(i.y.get())]), np.array([float(i.Vx.get()),float(i.Vy.get())])))
        w.destroy()

    global n
    a=[]
    w=Frame(root)
    w.pack()
    label_m =Label(w, text="mass").grid(row=0, column=1)
    label_x =Label(w, text="x").grid(row=0, column=2)
    label_y =Label(w, text="y").grid(row=0, column=3)
    label_Vx=Label(w, text="Vx").grid(row=0, column=4)
    label_Vy=Label(w, text="Vy").grid(row=0, column=5)
    label_r =Label(w, text="R").grid(row=0, column=6)
    label_obj=[]
    for i in range(n):
        label_obj.append(Label(w, text=str(i+1)).grid(row=i+1, column=0))
    entries=[]
    for i in range(n):
        entries.append(param(w, i))
    okbutton=Button(w, text="OK", command=get_param).grid(row=n+2, column=3, columnspan=2)
    w.wait_window()
    return a