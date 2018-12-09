#import Objects
from Setup import *
import Field
dt=0.1
stop=False


root=Tk()
root.title("Objects")
root.geometry("500x500")
root.resizable(True, True)
def close():
    root.destroy()
    root.quit()


canvas=Canvas(root, bg="white")
setup=Setup(root, canvas)
canvas.pack(fill="both", expand=True)
Field.start(root, canvas, setup, dt)

root.mainloop()