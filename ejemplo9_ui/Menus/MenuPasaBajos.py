import tkinter as tk
import Config


class MenuPasaBajos(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.parent = parent

        self.title = tk.Label(
            self,
            height=1,
            width=50,
            text="Configuración parámetros pasa bajo",
            font=Config.LARGE_FONT,
            background="#ffccd5"
        )

        self.title.pack(side=tk.TOP, fill=tk.BOTH)

        self.titlePsi = tk.Label(
            self,
            height=1,
            width=50,
            text="Epsilon",
            font=Config.SMALL_FONT,
            background="#ccffd5"
        )

        self.titlePsi.pack(side=tk.TOP, fill=tk.BOTH, pady=30)

        self.w1 = tk.Scale(self, from_=0, to=1, resolution = 0.01, orient=tk.HORIZONTAL)
        self.w1.pack(side=tk.TOP, fill=tk.BOTH)

        self.titleFo = tk.Label(
            self,
            height=1,
            width=50,
            text="Frecuencia de corte (kHz)",
            font=Config.SMALL_FONT,
            background="#ccffd5"
        )

        self.titleFo.pack(side=tk.TOP, fill=tk.BOTH, pady=30)

        self.w2 = tk.Scale(self, from_=0, to=100, resolution = 0.1, orient=tk.HORIZONTAL)
        self.w2.pack(side=tk.TOP, fill=tk.BOTH)

        self.buttonContinuar = tk.Button(
            self,
            height=2,
            width=50,
            text="Continuar",
            font=Config.SMALL_FONT,
            background="#ccffd5",
            command=self.continuar
        )

        self.buttonContinuar.pack(side=tk.TOP, fill=tk.BOTH, pady=20)

    def continuar(self):
        pass

    def focus(self):
        pass
