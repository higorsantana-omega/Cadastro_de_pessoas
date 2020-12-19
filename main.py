from tkinter import ttk
from tkinter import *
from tkinter import filedialog
import os
from PIL import Image, ImageTk
import sqlite3

import Cadastro_clientes as GUI
import database



if __name__ == '__main__':
    database.InitDB()
    GUI.vp_start_gui()
