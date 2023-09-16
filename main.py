from tkinter import *

import customtkinter as ctk
from customtkinter import filedialog
from tkinter.messagebox import showinfo
import os
import webbrowser

root = ctk.CTk()  # create CTk window like you do with the Tk window
root.title("FOMMfIA-CTK")
ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark  # Themes: blue (default), dark-blue, green

root.geometry()
root.wm_attributes('-alpha',0.95)



ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
root.geometry()
root.option_add("*tearOff", FALSE)
root.resizable(False, False)

pathvideo = ""
pathphoto = ""
pathsave = ""
pathcheck = ""


def choose_video():
    global pathvideo
    pathvideo = filedialog.askopenfilename()
    video_btn.configure(fg_color = "green")


def choose_photo():
    global pathphoto
    pathphoto = filedialog.askopenfilename()
    photo_btn.configure(fg_color = "green")


def choose_save():
    global pathsave
    pathsave = filedialog.askdirectory()
    save_btn.configure(fg_color = "green")


def choose_check():
    global pathcheck
    pathcheck = filedialog.askopenfilename()
    check_btn.configure(fg_color = "green")


def start_request():
    global pathvideo, pathphoto, pathsave, pathcheck

    if cuda_checkbox.get() == 0:
        str_cuda = "--cpu"
    else:
        str_cuda = ""

    if adapt_checkbox.get() == 1:
        str_adapt = "--adapt_scale"
    else:
        str_adapt = ""

    if cord_checkbox.get() == 1:
        str_rel = "--relative"
    else:
        str_rel = ""

    if dv_checkbox.get() == 1:
        str_audio = "--audio"
    else:
        str_audio = ""

    os.system(
        f"python first-order-model/demo.py  --config first-order-model/config/{combobox.get()}.yaml --driving_video {pathvideo} --result_video {pathsave}/result.mp4 --source_image {pathphoto} --checkpoint {pathcheck} {str_rel} {str_adapt} {str_cuda} {str_audio}")
    video_btn.configure(fg_color = "#14375e")
    photo_btn.configure(fg_color = "#14375e")
    save_btn.configure(fg_color = "#14375e")
    check_btn.configure(fg_color = "#14375e")

    showinfo(title="Готово", message=f"Видео сгенериванно и находится в каталоге: {pathsave}")

    pathvideo = ""
    pathphoto = ""
    pathsave = ""
    pathcheck = ""


super_label = ctk.CTkLabel(root, text_color='#AAAAAA', text="First Order Motion Model for Image Animation with CTK",
                           font=('Arial', 32))
super_label.grid(column=0, row=0, columnspan=38, rowspan=2)

video_label = ctk.CTkLabel(root, text_color='#DDDDDD', text="Video/Видео")
video_label.grid(column=0, row=3)

video_btn = ctk.CTkButton(root, text="Выберите файл", command=choose_video, height=50)
video_btn.grid(column=0, row=4, rowspan=2)

photo_label = ctk.CTkLabel(root, text_color='#DDDDDD', text="Photo/Фото")
photo_label.grid(column=0, row=6)

photo_btn = ctk.CTkButton(root, text="Выберите файл", command=choose_photo, height=50)
photo_btn.grid(column=0, row=7, rowspan=2)

model_label = ctk.CTkLabel(root, text_color='#DDDDDD', text="Checkpoint")
model_label.grid(column=0, row=9)

check_btn = ctk.CTkButton(root, text="Выберите файл", command=choose_check)
check_btn.grid(column=0, row=10)

download_check_btn = ctk.CTkButton(root, text="Скачать checkpoint", command= lambda: webbrowser.open("https://drive.google.com/drive/folders/1PyQJmkdCsAkOYwUyaj_l-l0as-iLDgeH", new=1))
download_check_btn.grid(column=0, row=12)

check_label = ctk.CTkLabel(root, text_color='#DDDDDD', text="Save in/Сохранить в")
check_label.grid(column=0, row=14)

save_btn = ctk.CTkButton(root, text="Выберите директорию", command=choose_save)
save_btn.grid(column=0, row=15)

model_label = ctk.CTkLabel(root, text_color='#DDDDDD', text="Model/Модель")
model_label.grid(column=1, row=3)

combobox = ctk.CTkComboBox(root,
                           values=["bair-256", "fashion-256", 'mgif-256', 'nemo-256', 'taichi-256', 'taichi-adv-256',
                                   'vox-256', 'vox-adv-256'])
combobox.grid(column=1, row=4)

text_label=ctk.CTkLabel(root, text="", font=("Arial", 10), text_color="gray")
text_label.grid(column=1, row=5, rowspan=10)

cuda_checkbox = ctk.CTkCheckBox(root, text="Использовать ядра Cuda (поддерживается не на всех видеокартах)")
cuda_checkbox.grid(column=32, row=3)

adapt_checkbox = ctk.CTkCheckBox(root, text="Адаптиваться под размеры исходника")
adapt_checkbox.grid(column=32, row=4, sticky=W)

cord_checkbox = ctk.CTkCheckBox(root, text="Отосительные координаты")
cord_checkbox.grid(column=32, row=5, sticky=W)

dv_checkbox = ctk.CTkCheckBox(root, text="Взять аудио из ведущего видео")
dv_checkbox.grid(column=32, row=6, sticky=W)

author_btn = ctk.CTkButton(root, text="By bolgaro4ka", command= lambda: webbrowser.open("https://github.com/bolgaro4ka", new=1))
author_btn.grid(column=32, row=8, sticky=E)

start_btn = ctk.CTkButton(root, text="Начать генерацию", width=430, height=150, fg_color='green', hover_color='red', command=start_request)
start_btn.grid(column=32, row=9, rowspan=15, sticky=E)

root.mainloop()
