from tkinter import *
import numpy as np
import Objects
import time


class Setup:
    def __init__(self, root, canvas):
        canvas.pack_forget()
        self.n=2
        self.F = self.initial(root)
        canvas.config(state=NORMAL)
        self.a = self.object_list(root, canvas)

    def initial(self, root):
        def get_amount():
            F[0] = float(entry_x.get())
            F[1] = float(entry_y.get())
            w.destroy()

        F = np.array([0, 0], dtype=float)
        w = Frame(root)
        w.pack()
        okbutton = Button(w, text="OK", command=get_amount)
        okbutton.pack()
        label_set_force = Label(w, text="Enter the constant force value.")
        label_set_force.pack()
        label_x = Label(w, text="x")
        label_x.pack(side="left")
        label_y = Label(w, text="y")
        label_y.pack(side="right")
        entry_x = Entry(w)
        entry_x.insert(0, str(F[0]))
        entry_x.pack(side="left")
        entry_y = Entry(w)
        entry_y.insert(0, str(F[0]))
        entry_y.pack(side="left")
        w.wait_window()
        return F
    
    def object_list(self, root, canvas):
        canvas.pack(fill="both", expand=True)
        a=[]
        def start():
            w.destroy()
            
        def random():
            def randomise():
                self.n=int(entry.get())
                for i in range(self.n):
                    m=np.random.randint(1, 5000)
                    r=np.random.randint(1, 10)
                    p=np.array(np.random.randint(1, 450, 2), dtype=float)
                    v=np.array(np.random.randint(1, 50, 2), dtype=float)
                    a.append(Objects.Object(canvas, m, r, p, v))
                canvas.pack(fill="both", expand=True)
                start()
            np.random.seed(int(time.time()))
            
            canvas.pack_forget()
            add_button.destroy()
            start_button.destroy()
            random_button.destroy()
            
            label=Label(w, text="Enter the amount of objects").pack()
            entry=Entry(w)
            entry.insert(0, str(self.n))
            entry.pack(fill="both", expand=True)
            okbutton=Button(w, text="OK", command=randomise)
            okbutton.pack()
            
        w=Frame(root)
        w.pack()
        
        def add_object():
            w2=Frame(root)
            w2.pack()
            start_button.config(state=DISABLED)
            add_button.config(state=DISABLED)
            random_button.config(state=DISABLED)
            def click(e):
                def get_param():
                    a.append(Objects.Object(canvas, float(entry_m.get()), float(entry_r.get()), np.array([canvas.canvasx(e.x), canvas.canvasy(e.y)], dtype=float), np.array([float(entry_Vx.get()), float(entry_Vy.get())]), np.array(self.F, dtype=float)))
                    w2.destroy()
                    start_button.config(state=NORMAL)
                    add_button.config(state=NORMAL)
                    random_button.config(state=NORMAL)
                    
                def cancel():
                    start_button.config(state=NORMAL)
                    add_button.config(state=NORMAL)
                    random_button.config(state=NORMAL)
                    w2.destroy()
                    
                #x=e.x
                #y=e.y
                canvas.unbind(funcid)
                label_m = Label(w2, text="mass").grid(row=0, column=0)
                label_Vx = Label(w2, text="Vx").grid(row=0, column=1)
                label_Vy = Label(w2, text="Vy").grid(row=0, column=2)
                label_r = Label(w2, text="R").grid(row=0, column=3)
                entry_m=Entry(w2, width=10)
                entry_m.grid(row=1, column=0)
                entry_Vx=Entry(w2, width=10)
                entry_Vx.insert(0, '0')
                entry_Vx.grid(row=1, column=1)
                entry_Vy= Entry(w2, width=10)
                entry_Vy.insert(0, '0')
                entry_Vy.grid(row=1, column=2)
                entry_r = Entry(w2, width=10)
                entry_r.insert(0, '5')
                entry_r.grid(row=1, column=3)
                okbutton=Button(w2, text="OK", command=get_param)
                cancel_button=Button(w2, text="Cancel", command=cancel)
                okbutton.grid(row=2, column=1)
                cancel_button.grid(row=2, column=2)

            funcid=canvas.bind("<Button-1>", click)
            return 0
        random_button=Button(w, text="Random", command=random)
        add_button=Button(w, text="Add object", command=add_object)
        add_button.pack()
        random_button.pack()
        start_button=Button(w, text="Start", command=start)
        start_button.pack()
        
            
        w.wait_window()
        return a
