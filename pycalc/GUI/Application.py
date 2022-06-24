from tkinter import Tk
from ..kernel.Сalculator import Calculator


class Application(Tk, Calculator):
    def __init__(self):
        Tk.__init__(self)
        Calculator.__init__(self)
