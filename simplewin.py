# создание программы в стиле GUI
import tkinter as gui
from const import *

# создать главное окно программы
win = gui.Tk()
# задать размер окна
win.geometry(INIT_WIN_SIZE)
# новый заголовок окна
win.title(MAIN_TITLE)

# создать систему главного меню
main_menu = gui.Menu (win)
# создать первую группу
file_item = gui.Menu (main_menu)
# пункты первой группы
file_item.add_command(label='Новый')
file_item.add_command(label='Открыть...')
file_item.add_command(label='Сохранить как...')
# разделитель
file_item.add_separator()
file_item.add_command(label='Выйти из программы')
# подключить первую группу к главному меню
main_menu.add_cascade(label='Файл', menu=file_item)

# подключить систему меню к окну программы
win.config(menu=main_menu)

# вывести окно на экран
win.mainloop()
