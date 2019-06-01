
### Hecho por Ariel Nowik

# Copyright [yyyy] [name of copyright owner]
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# Ejemplo ui con tkinter Electrotecnia I 22.02

# Este programa es un ejemplo sobre como pueden estructurar una interfaz gráfica en python
# con las funcionalidades necesarias para el tp final. Pueden utilizarlo, modificarlo o integrarlo con otro programa
# de la forma que les parezca más apropieda.

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
    # UI hereda de tk.Tk que es la entidad principal de tkinter
    # UI es el administrador de nuestra interfaz gráfica

    def __init__(self, **kwargs):
        # kwargs tiene todos los parametros que se hayan colocado

        # llamamos a el constructor del padre, tk.Tk
        super(UI, self).__init__(**kwargs) # le damos los mismos parámetros con los que se llamo UI

        # funciones que configuran como es la interfaz gráfica que vamos a utilizar
        self.protocol('WM_DELETE_WINDOW', self.exitFunction)
        self.title("Ejemplo gui 01")
        self.resizable(width=False, height=False)
        self.minsize(width=700, height=500)

        # container es el widget "maestro".
        # Nuestro programa funciona mediante el agregado y el sacado de widgets a container
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)

        self.frames = {}

        for frame in frames:
            # cargamos a la memoria la información todos los frames
            self.frames[frame] = frame(self.container, self)
            self.frames[frame].grid_propagate(True)
            self.frames[frame].grid(row=0, column=0, sticky=E + W + N + S)

        # comenzamos la aplicación en startFrame que es la variable que nos indica donde empezar
        self.showFrame(startFrame)

    def showFrame(self, frame):
        # comenzar a mostrar un frame en particular
        self.frames[frame].focus()
        frame = self.frames[frame]
        frame.tkraise()
        self.frame = frame

    def getCurrentFrame(self):
        # obtener el frame actual
        return self.frame

    def run(self):
        # comenzar el programa
        # el loop lo controla tkinter, llamando "mainloop" se lo entregamos
        self.mainloop()

    def exitFunction(self):
        # funciones de tkinter que administran que debe suceder cuando salimos del programa
        self.quit()
        self.destroy()


if __name__ == "__main__":
    UI().run()
