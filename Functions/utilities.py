import sys
import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'models/'))
from Functions.models import utilFunctions as UF
from Functions.transformations_interface import stftMorph_function as sT


# Functions
def play_song():
    try:
        filename = filedialog.askopenfilename()
        UF.wavplay(filename)

    except Exception as e:
        print(e)

def browse_file1(master):
    try:
        #
        filename = filedialog.askopenfilename(title="Please Select a File")
        master.equalizer_frame.filelocation1.delete(0, END)
        master.equalizer_frame.filelocation1.insert(0, filename)
        master.stretcher_frame.filelocation1.delete(0, END)
        master.stretcher_frame.filelocation1.insert(0, filename)

    except Exception as e:
        messagebox.showerror("We can not open that file")

def browse_file2(master):
    try:
        filename = filedialog.askopenfilename(title="Please Select a File")
        master.filelocation2.delete(0, END)
        master.filelocation2.insert(0, filename)

    except Exception as e:
        print(e)

def transformation_synthesis(master):
    try:
        inputFile1 = master.filelocation1.get()
        inputFile2 = master.filelocation2.get()
        window1 = master.w1_type.get()
        window2 = master.w2_type.get()
        M1 = int(master.M1.get())
        M2 = int(master.M2.get())
        N1 = int(master.N1.get())
        N2 = int(master.N2.get())
        H1 = int(master.H1.get())
        smoothf = float(master.smoothf.get())
        balancef = float(master.balancef.get())
        y, fs = sT.main(inputFile1, inputFile2, window1, window2, M1, M2, N1, N2, H1, smoothf, balancef)
        save_audio(y, fs)

    except ValueError:
        messagebox.showerror("Input values error")

def save_audio(y, fs):
    try:
        outputFile = filedialog.asksaveasfile()
        UF.wavwrite(y, fs, outputFile.name + '_stftMorph.wav')

    except Exception:
        messagebox.showerror("We can not save this file")

def button_event():
    print("Button pressed")

def change_to_frame1(master):
    try:
        master.equalizer_frame.tkraise()

    except Exception:
        messagebox.showerror("Something went wrong")

def change_to_frame2(master):
    try:
        master.stretcher_frame.tkraise()

    except Exception:
        messagebox.showerror("Something went wrong")
