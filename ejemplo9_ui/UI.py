import tkinter as tk
from tkinter import *
from Menus.MenuSelectOrder import MenuSelectOrder
from Menus.MenuPrimerOrden import MenuPrimerOrden
from Menus.MenuPasaBajos import MenuPasaBajos
from Menus.MenuModo import MenuModo
from Menus.MenuInputOutput import MenuInputOutput


frames = [
    MenuSelectOrder,
    MenuPrimerOrden,
    MenuPasaBajos,
    MenuModo,
    MenuInputOutput
]

startFrame = MenuSelectOrder


class UI(tk.Tk):
    def __init__(self, **kwargs):
        super(UI, self).__init__(**kwargs)

        self.protocol('WM_DELETE_WINDOW', self.exitFunction)
        self.title("Ejemplo gui 01")
        self.resizable(width=False, height=False)
        self.minsize(width=700, height=500)
        #self.maxsize(width=800, height=400)

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)

        self.frames = {}

        for frame in frames:
            self.frames[frame] = frame(self.container, self)
            self.frames[frame].grid_propagate(True)
            self.frames[frame].grid(row=0, column=0, sticky=E + W + N + S)

        self.showFrame(startFrame)

    def showFrame(self, frame): # comenzar a mostrar un frame en particular
        self.frames[frame].focus()
        frame = self.frames[frame]
        frame.tkraise()
        self.frame = frame

    def getCurrentFrame(self):
        return self.frame

    def run(self):
        self.mainloop()

    def exitFunction(self):
        self.quit()
        self.destroy()


if __name__ == "__main__":
    UI().run()
