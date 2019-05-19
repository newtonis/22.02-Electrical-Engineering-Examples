import tkinter as tk
import Config
from UserInput import userInput

from Menus.MenuPrimerOrden import MenuPrimerOrden


class MenuSelectOrder(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.parent = parent

        self.title = tk.Label(
            self,
            height=1,
            width=50,
            text="Seleccionar orden del filtro",
            font=Config.LARGE_FONT,
            background="#ffccd5"
        )

        self.title.pack(side=tk.TOP, fill=tk.BOTH)

        self.button1order = tk.Button(
            self,
            height=3,
            width=30,
            text="Filtro de 1er orden",
            font=Config.SMALL_FONT,
            background="#ccffd5",
            command=self.boton1OrdenPresionado

        )
        self.button1order.pack(side=tk.TOP, expand=1, fill=tk.BOTH, pady=100)

        self.button2order = tk.Button(
            self,
            height=3,
            width=30,
            text="Filtro de 2do orden",
            font=Config.SMALL_FONT,
            background="#ccffd5",
            command=self.boton2OrdenPresionado
        )

        self.button2order.pack(side=tk.TOP, expand=1, fill=tk.BOTH, pady=100)

    def boton1OrdenPresionado(self):
        self.controller.showFrame(MenuPrimerOrden)
        userInput["order"] = "1er orden"

    def boton2OrdenPresionado(self):
        pass

    def focus(self):
        pass
