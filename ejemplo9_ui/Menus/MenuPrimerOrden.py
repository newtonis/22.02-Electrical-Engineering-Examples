import tkinter as tk
import Config
from Menus.MenuPasaBajos import MenuPasaBajos
from UserInput import userInput


class MenuPrimerOrden(tk.Frame):  # heredamos de tk.Frame, padre de MenuPrimerOrden
    def __init__(self, parent, controller):
        # parent representa el Frame principal del programa, tenemos que indicarle
        # cuando MenuInputOutput será dibujado

        # controller lo utilizamos cuando necesitamos que el controlador principal del programa haga algo

        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.parent = parent

        # creamos widgets y los agregamos a la pantalla con pack
        self.title = tk.Label(
            self,
            height=1,
            width=50,
            text="Pasa bajos",
            font=Config.LARGE_FONT,
            background="#ffccd5"
        )

        self.title.pack(side=tk.TOP, fill=tk.BOTH)

        self.button1order = tk.Button(
            self,
            height=3,
            width=50,
            text="Filtro de 1er orden",
            font=Config.SMALL_FONT,
            background="#ccffd5",
            command=self.gotoMenuPasaBajos

        )
        self.button1order.pack(side=tk.TOP, expand=1, fill=tk.BOTH, pady=100)

    def gotoMenuPasaBajos(self):
        # cambiamos de frame
        self.controller.showFrame(MenuPasaBajos)
        userInput["mode"] = "pasa bajos"

    def focus(self):
        pass

