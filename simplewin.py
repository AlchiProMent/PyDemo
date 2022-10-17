# создание программы в стиле GUI
import tkinter as gui
from const import *

# создать главное окно программы
win = gui.Tk()
# задать размер окна
win.geometry(INIT_WIN_SIZE)
# новый заголовок окна
win.title(MAIN_TITLE)
# вывести окно на экран
win.mainloop()
