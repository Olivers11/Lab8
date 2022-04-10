from tkinter import *

class Window:

    def __init__(self, temp, master):
        self.screen = master
        self.title = Label(master, text="Temperatura", font=('Arial',20),foreground="green").place(x = 140, y = 80)
        self.temperature_text = StringVar()
        self.temperature_text.set(temp + "°C")
        self.drawMessage()

    def drawMessage(self):
        self.msg = Label(self.screen, textvariable=self.temperature_text, font=('Arial', 18)).place(x = 180, y = 130)


    def reload(self, text):
        self.temperature_text.set(text + "°C")
        self.drawMessage()


class App:
    def __init__(self, text):
        self.root = Tk()
        self.root.geometry("400x400")
        self._run_(text)

    def _run_(self, text):
        self.window = Window(text, self.root)
        self.root.mainloop()
    
    def change_temp(self, text):
        self.window.reload(text)


