from tkinter import *


class Window:

    def __init__(self, temp, master):
        self.title = Label(master, text="Temperatura", font=('Arial',20),
                foreground="green").place(x = 140, y = 80)
        self.msg = Label(master, text=temp + "°C", font=('Arial', 18)).place(x = 180, y = 130)


class App:
    def __init__(self, text):
        self.root = Tk()
        self.root.geometry("400x400")
        self._run_(text)

    def _run_(self, text):
        window = Window(text, self.root)
        self.root.mainloop()



