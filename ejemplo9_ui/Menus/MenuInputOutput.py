import tkinter as tk
import Config
from tkinter import *
from UserInput import userInput


from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
import matplotlib.pyplot as plt
from scipy import signal
from numpy import pi


class MenuInputOutput(tk.Frame):  # heredamos de tk.Frame, padre de MenuInputOutput
    def __init__(self, parent, controller):
        # parent representa el Frame principal del programa, tenemos que indicarle
        # cuando MenuInputOutput será dibujado

        # controller lo utilizamos cuando necesitamos que el controlador principal del programa haga algo

        # llamamos al constructor del padre de MenuInputOutput, que es tk.Frame
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.parent = parent

        self.title = tk.Label(
            self,
            height=1,
            width=50,
            text="Entrada - Salida gráfico",
            font=Config.LARGE_FONT,
            background="#ffccd5"
        )
        # con pack provocamos que los widgets se dibujen efectivamente en la pantalla
        self.title.pack(side=tk.TOP, fill=tk.BOTH)
        # creamos el canvas
        self.graph = Canvas(self)
        # creamos figura y ejes del gráfico de maplotlib
        self.fig, (self.ax1, self.ax2) = plt.subplots(nrows=2, sharex=True)
        # Estos dos objetos dataPlot y nav son el puente entre maplotlib y tkinter
        self.dataPlot = FigureCanvasTkAgg(self.fig, master=self.graph)
        self.nav = NavigationToolbar2Tk(self.dataPlot, self.graph)
        self.dataPlot.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        self.dataPlot._tkcanvas.pack(side=BOTTOM, fill=X, expand=1)

        self.graph.pack(side=TOP, expand=1, fill=BOTH)
        # boton para volver
        self.backButton = tk.Button(
            self,
            height=2,
            width=50,
            text="Volver",
            font=Config.SMALL_FONT,
            background="#cfffd5",
            command=self.goBack
        )
        self.backButton.pack(side=tk.TOP, fill=tk.BOTH)

    def focus(self):
        self.ax1.clear()

        # calcuamos gráficos acorde a la configuracion seleccionada
        # userInput tiene la información que fue insertada en el Frame anterior
        self.ax1.plot(userInput["input"]["t"], userInput["input"]["y"])
        self.ax1.minorticks_on()
        self.ax1.grid(which='major', linestyle='-', linewidth=0.3, color='black')
        self.ax1.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

        # Aca cambiaría la configuración según lo que se configuró en el frame anterior
        if userInput["order"] == "1er orden":
            if userInput["mode"] == "pasa bajos":
                self.plotPasaBajos1erOrden()

        self.dataPlot.draw()

    def plotPasaBajos1erOrden(self):
        f0 = userInput["f0"]

        w0 = 2 * pi * f0
        print("frecuencia de corte = ", f0)

        sys = signal.lti([w0], [1, w0])

        output = dict()

        # https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.lsim.html#scipy.signal.lsim

        output["t"], output["y"], m = signal.lsim(sys, userInput["input"]["y"], userInput["input"]["t"])

        self.ax2.clear()

        self.ax2.plot(output["t"], output["y"], color="orange")
        self.ax2.minorticks_on()
        self.ax2.grid(which='major', linestyle='-', linewidth=0.3, color='black')
        self.ax2.grid(which='minor', linestyle=':', linewidth=0.1, color='black')

    def goBack(self):
        # evitamos dependencias circulares, importamos solo cuando es necesario
        from Menus.MenuSelectOrder import MenuSelectOrder

        self.controller.showFrame(MenuSelectOrder)
