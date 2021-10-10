import pyautogui
from PIL import Image
from pytesseract import *
from gtts import gTTS
import os
from tkinter import *
import tkinter.messagebox
import numpy as np
from PIL import ImageTk,Image
from tkinter import filedialog
from pickle import dump
import os
import tflearn
import gc
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.conv import  conv_2d, max_pool_2d
from tflearn.layers.estimator import regression
import cv2


def open_img() :
    global path
    pytesseract.tesseract_cmd = r'C:\Users\3shry\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

    canvas.delete("all")

    img_path = filedialog.askopenfilename()
    path=img_path
    img = Image.open(img_path)
    res = pytesseract.image_to_string(img)

    # Language we want to use
    language = 'en'

    myobj = gTTS(text=res, lang=language, slow=False)

    myobj.save("output.mp3")

    # Play the converted file
    os.system("start output.mp3")

    img = img.resize((1200, 650), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, anchor=NW, image=img)



    gc.collect()
    form.mainloop()


def main():

    ################GUI##################

    img = Image.open("1200px-Open_book_nae_02.svg.png")
    img = ImageTk.PhotoImage(img)
    canvas.create_image(10, 10, anchor=NW, image=img)

    Upload_butt = Button(text="   Upload   ", command=open_img)
    Upload_butt.place(x=550, y=600)


    form.mainloop()


if __name__ == '__main__':
    form = Tk()
    canvas = Canvas(form, width=1200, height=650)
    canvas.pack()
    main()


