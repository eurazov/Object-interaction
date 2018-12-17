from Setup import *
from tkinter import *


class Field:
    def __init__(self):
        self.root=Tk()
        self.root.title("Objects")
        self.root.geometry("500x500")
        self.root.resizable(True, True)
        self.canvas = Canvas(self.root, bg="white", state=DISABLED)
        self.setup = Setup(self.root, self.canvas)
        self.stop=False
        self.dt=0.1
        self.start()
        self.root.mainloop()

    def close(self):
        self.root.destroy()
        self.root.quit()

    def update_field(self):
        for i in range(len(self.setup.a)):
            self.setup.a[i].move(self.canvas, self.dt)
            self.setup.a[i].accelerate(self.dt)
            self.setup.a[i].force = np.array(self.setup.F, dtype=float)
        i = 0
        while i < len(self.setup.a):
            j = i + 1
            while j < len(self.setup.a):
                if self.setup.a[i].collision(self.setup.a[j], self.canvas):
                    self.canvas.delete(self.setup.a[j].id)
                    del self.setup.a[j]
                    break
                self.setup.a[i].interact(self.setup.a[j])
                j += 1
            i += 1
        if not self.stop:
            self.root.after(round(self.dt*1000), self.update_field)

    def start(self):
        self.stop=False
        def stop_command():
            self.stop = not self.stop
            if self.stop:
                btn.config(text="Start")
                setup_btn.config(state=NORMAL)
            else:
                btn.config(text="Pause")
                setup_btn.config(state=DISABLED)
                self.update_field()

        def setup_command():
            self.canvas.config(state=DISABLED)
            setup_btn.destroy()
            btn.destroy()
            for i in self.setup.a:
                self.canvas.delete(i.id)
            self.setup = Setup(self.root, self.canvas)
            self.canvas.config(state=NORMAL)

            self.start()
        btn = Button(self.root, text="Pause", command=stop_command)
        btn.pack(side="right")
        setup_btn = Button(self.root, text="Setup", state=DISABLED, command=setup_command)
        setup_btn.pack(side="left")
        self.update_field()