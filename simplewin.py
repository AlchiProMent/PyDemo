# создание программы в стиле GUI
import tkinter as gui
from tkinter import messagebox
from tkinter import filedialog
from const import *

def new_click():
    # обработчик щелчка по пункту НОВЫЙ
    messagebox.showinfo('Пункт меню', 'Новый')

def open_click():
    # обработчик щелчка по пункту ОТКРЫТЬ
    file = filedialog.askopenfile(filetypes=( ('Python файл', '*.py'),('Текстовый файл','*.txt'),('Все файлы','*.*') ))
    # в заголовке окна поместить имя файла
    win.title(file.name)

def save_click():
    # обработчик щелчка по пункту СОХРАНИТЬ
    filedialog.asksaveasfilename()

def exit_click():
    # обработчик щелчка по пункту ВЫЙТИ ИЗ ПРОГРАММЫ
    win.quit()

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
file_item.add_command(label=FILE_NEW, command=new_click)
file_item.add_command(label=FILE_OPEN, command=open_click)
file_item.add_command(label=FILE_SAVE, command=save_click)
# разделитель
file_item.add_separator()
file_item.add_command(label=FILE_EXIT, command=exit_click)
# подключить первую группу к главному меню
main_menu.add_cascade(label=MAIN_ITEM_FILE, menu=file_item)

# подключить систему меню к окну программы
win.config(menu=main_menu)

# вывести окно на экран
win.mainloop()
