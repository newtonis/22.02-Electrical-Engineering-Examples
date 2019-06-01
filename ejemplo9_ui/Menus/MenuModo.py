import tkinter as tk
import Config
from Menus.MenuInputOutput import MenuInputOutput
from UserInput import userInput
import numpy as np


class MenuModo(tk.Frame):  # heredamos de tk.Frame, padre de MenuModo
    def __init__(self, parent, controller):
        # parent representa el Frame principal del programa, tenemos que indicarle
        # cuando MenuInputOutput será dibujado

        # controller lo utilizamos cuando necesitamos que el controlador principal del programa haga algo

        # llamamos al constructor
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.parent = parent
        # agregamos un boton y un titulo
        self.title = tk.Label(
            self,
            height=1,
            width=50,
            text="Seleccionar modo",
            font=Config.LARGE_FONT,
            background="#ffccd5"
        )

        self.title.pack(side=tk.TOP, fill=tk.BOTH)

        self.buttonEntradaSalida = tk.Button(
            self,
            height=2,
            width=50,
            text="Pulso periódico",
            font=Config.SMALL_FONT,
            background="#ccffd5",
            command=self.modoPulsoPeriodico
        )

        self.buttonEntradaSalida.pack(side=tk.TOP, fill=tk.BOTH, pady=20)

    def modoPulsoPeriodico(self):
        paso = 1e-6
        # generamos una señal de pulso periódico que arranque en t = 0.01 con f=1khz
        t = np.arange(0, 0.01, paso) # 1us de presición
        N = len(t)

        freq = 1e3
        period = 1 / freq
        periodSamples = int(period / paso)

        # este codigo genera una señal cuadrada,
        cuadrada = np.where(np.arange(N) % periodSamples < periodSamples/2, -0.5, 0.5)

        # para que la señal no empiece de golpe y visualmente se vea mejor su comienzo
        for i in range(2 * periodSamples):
            cuadrada[i] = 0

        # cargamos a la memoria la entrada seleccionada. Esta información será utilizada
        # por MenuInputOutput
        userInput["input"] = {
            "y": cuadrada,
            "t": t
        }
        # cambiamos el frame que esta actualmente abierto
        self.controller.showFrame(MenuInputOutput)
