import datetime
import socket, os, sys
import tkinter as tk
from PIL import Image, ImageTk
from PIL import ImageGrab as ImageGrab_PIL
import pyscreenshot as ImageGrab

def resource_path(relative_path):
#""" Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def key(event=None):
    root.bell()

    # small delay to allow tk window to fade on LCDs
    for x in range(1000000):
        x = x + 77

    # th is will grab the whole screen display and save it to a file
    if os.name == 'nt':
        img = ImageGrab_PIL.grab()
    else:
        img = ImageGrab.grab()

    hostname = socket.gethostname()
    nomefile = str(hostname)+'__'+str(datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S"))+".png"
    pathFile = resource_path(nomefile)
    img.save(pathFile)
    # this will grab a 400 pixel wide and 300 pixel heigh partion
    # upper left corner screen coordinates x=0, y=0
    ImageFile = Image.open(pathFile)
    ImageFile = ImageFile.resize((200, 200), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(ImageFile)
    panel = tk.Label(root, image=img, bg="red", pady=0, padx=0)
    panel.photo = img
    panel.grid(row=1, columnspan=3)
    tk.Label(root, text=pathFile, bg='yellow', pady=30, padx=10).grid(row=2, columnspan=3)

    return

root = tk.Tk()
root.configure(background='lightgrey')
root.resizable(False, False)
root.title('Screen Image Grabber')
hostname = socket.gethostname()
str1 = """\
Cattura l'immagine e rinomina lo screenshot secondo il seguente modello: 
"""+ str(hostname)+'__%m_%d_%Y_%H_%M_%S.png'

tk.Label(root, text=str1, bg='yellow', pady=30, padx=10).grid(row=0, columnspan=3)
tk.Canvas(root, width=300, height=300, bg="yellow").grid(row=1, columnspan=3, pady=20)
#tk.Label(root, text='', bg='yellow', pady=30, padx=10).grid(row=2, columnspan=3)
tk.Button(root, text ="Cattura", command = key).grid(row=3, columnspan=3,pady=15)

#root.bind('<Key>', key)
root.mainloop()

