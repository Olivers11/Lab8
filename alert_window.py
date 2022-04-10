from tkinter import *
from PIL import ImageTk, Image
from itertools import count, cycle
import tkinter as tk
 
class ImageLabel(tk.Label):
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []
 
        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)
 
        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100
 
        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()
 
    def unload(self):
        self.config(image=None)
        self.frames = None
 
    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)

def show_message():
    window = Tk()
    window.geometry("700x500")
    label = ImageLabel(window)
    label.pack()
    label.load("./alert.gif")
    label_msg = Label(window, text="PANIK!!!!", font=('Arial', 14))
    label_msg.pack()
    label.mainloop()



