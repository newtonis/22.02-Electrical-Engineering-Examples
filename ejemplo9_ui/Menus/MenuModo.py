import tkinter as tk
import Config
from Menus.MenuInputOutput import MenuInputOutput
from UserInput import userInput
import numpy as np


class MenuModo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.parent = parent

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

        cuadrada = np.where(np.arange(N) % periodSamples < periodSamples/2,-0.5,0.5)

        for i in range(2 * periodSamples):
            cuadrada[i] = 0



        userInput["input"] = {
            "y": cuadrada,
            "t": t
        }

        self.controller.showFrame(MenuInputOutput)
