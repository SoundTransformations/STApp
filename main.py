import os
import sys

from tkinter import *
import tkinter as tk
from tkinter import ttk
import customtkinter
from tkinter import filedialog
from tkinter import messagebox

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Functions/models/'))
from Functions.models import utilFunctions as UF
from Functions.transformations_interface import stftMorph_function as sT

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


#Albert
#Andrea
#Nil
#Paula
#Functions
def play_song():
    filename = filedialog.askopenfilename()
    UF.wavplay(filename)

def browse_file1():
    try:
        #
        filename = filedialog.askopenfilename(title="Please Select a File")
        master.frame_right.filelocation1.delete(0, END)
        master.frame_right.filelocation1.insert(0,filename)
        master.frame_right2.filelocation1.delete(0, END)
        master.frame_right2.filelocation1.insert(0, filename)

    except Exception as e:
        print(e)

def browse_file2():
    try:
        filename = filedialog.askopenfilename(title="Please Select a File")
        master.filelocation2.delete(0, END)
        master.filelocation2.insert(0,filename)

    except Exception as e:
        print(e)

def transformation_synthesis():
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
        save_audio(y,fs)


    except ValueError as errorMessage:
        messagebox.showerror("Input values error", errorMessage)

def save_audio(y,fs):
    outputFile = filedialog.asksaveasfile()
    print(outputFile.name + '_stftMorph.wav')
    #outputFile = 'Functions/transformations_interface/output_sounds/' + os.path.basename(inputFile1)[:-4] + '_stftMorph.wav'
    UF.wavwrite(y, fs, outputFile.name + '_stftMorph.wav')

def button_event():
    print("Button pressed")

# Define a function for switching the frames
def change_to_frame1():
    master.frame_right.tkraise()
    #master.frame_right2.grid_forget()

def change_to_frame2():
    master.frame_right2.tkraise()
    #master.frame_right.grid_forget()

def get_current_value1():
    return '{: .2f}'.format(current_value1.get())

def slider1_changed(event):
    value_label1.configure(text=get_current_value1())

def get_current_value2():
    return '{: .2f}'.format(current_value2.get())

def slider2_changed(event):
    value_label2.configure(text=get_current_value2())

#Initialize the master root as a Tkinter interface

#master = Tk()
master = customtkinter.CTk()
master.title("Sound Transformations App")

#Set the size of the window
master.geometry("780x520")


## CREATE THREE FRAMES

#Configure grid layout (2x1)
master.grid_columnconfigure(1, weight=1)
master.grid_rowconfigure(0, weight=1)

#Create the Menu Selector Frame
master.frame_left = customtkinter.CTkFrame(master=master, width=180, corner_radius=0)
master.frame_left.grid(row=0, column=0, sticky="nswe")

#Create two possible frames (Equalizer and Strethcer)
master.frame_right2 = customtkinter.CTkFrame(master=master)
master.frame_right2.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
master.frame_right = customtkinter.CTkFrame(master=master)
master.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)



## CONFIGURE THE MENU SELECTOR FRAME

# configure grid layout (1x11)
master.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
master.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
master.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
master.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

#Add a switch
#master.switch_2 = customtkinter.CTkSwitch(master=master.frame_left,text="Dark Mode",command=change_mode)
#master.switch_2.grid(row=10, column=0, pady=10, padx=20, sticky="w")

#Add a Label
master.label_1 = customtkinter.CTkLabel(master=master.frame_left,text="STApp",text_font=("Roboto Medium", -16))  # font name and size in px
master.label_1.grid(row=1, column=0, pady=10, padx=10)

#Add a button
master.button_1 = customtkinter.CTkButton(master=master.frame_left,text="Equalizer",fg_color=("gray75", "gray30"),command=change_to_frame1)
master.button_1.grid(row=2, column=0, pady=10, padx=20)

#Add a second button
master.button_2 = customtkinter.CTkButton(master=master.frame_left,text="Stretcher",fg_color=("gray75", "gray30"),command=change_to_frame2)
master.button_2.grid(row=3, column=0, pady=10, padx=20)

#Add a third button
master.button_3 = customtkinter.CTkButton(master=master.frame_left,text="Relantizer",fg_color=("gray75", "gray30"),command=button_event)
master.button_3.grid(row=4, column=0, pady=10, padx=20)


## CONFIGURE THE EQUALIZER FRAME

#Configure grid layout (3x7)
master.frame_right2.rowconfigure((0, 1, 2, 3), weight=1)
master.frame_right2.rowconfigure(7, weight=10)
master.frame_right2.columnconfigure((0, 1), weight=1)
master.frame_right2.columnconfigure(2, weight=0)

## INPUT FILE 1
master.label_1 = customtkinter.CTkLabel(master=master.frame_right2,text="File1:",text_font=("Roboto Medium", -16), fg_color=("white", "gray30"), width = 30)  # font name and size in px
master.label_1.grid(row=0, column=0, pady=5, padx=50, sticky="w")

master.frame_right2.filelocation1 = customtkinter.CTkEntry(master=master.frame_right2,width=10,placeholder_text="Path to the first input file") #TEXTBOX TO PRINT PATH OF THE SOUND FILE
master.frame_right2.filelocation1.grid(row=0, column=0, columnspan=2, pady=5, padx=(120,200), sticky="we")
master.frame_right2.filelocation1.focus_set()

#Button to browse the input file 1
open_file1 = customtkinter.CTkButton(master.frame_right2, text="...", width = 3, command= browse_file1)
open_file1.grid(row=0, column=0, columnspan=2, sticky="e", padx=(150, 160), pady=5)

#Button to play the input file 1
preview1 =customtkinter.CTkButton(master.frame_right2, text="Play!",width = 3, command=lambda: UF.wavplay(master.frame_right2.filelocation1.get()),fg_color=("gray75", "gray30"), hover_color = "green")
preview1.grid(row=0, column=0, columnspan = 3, sticky="e", padx=(250,100), pady=5)


#SLIDERS of the EQUALIZER
style = ttk.Style()
style.configure("TScale", background="gray18")

master.label_6 = customtkinter.CTkLabel(master=master.frame_right,text="30 Hz",text_font=("Roboto Medium", -12), fg_color=("white", "gray30"), width = 30)  # font name and size in px
master.label_6.grid(row=2, column=0, pady=0, padx=50, sticky="w")

# slider current value
current_value1 = tk.DoubleVar()
slider_5 = ttk.Scale(master.frame_right,from_ = 100, to = 0, orient = VERTICAL, style="TScale", command = slider1_changed, variable = current_value1)
slider_5.grid(row=1, column=0,pady=0, padx=65, sticky="w")

# Value label
value_label1 = ttk.Label(master.frame_right,text=get_current_value1(), background = "gray18", justify="center", foreground="white")
value_label1.grid(row=1,column = 0, pady=0, padx=105,sticky='w')


master.label_7 = customtkinter.CTkLabel(master=master.frame_right,text="60 Hz",text_font=("Roboto Medium", -12), fg_color=("white", "gray30"), width = 30)  # font name and size in px
master.label_7.grid(row=2, column=0, pady=0, padx=150, sticky="w")

# slider current value
current_value2 = tk.DoubleVar()

slider_6 = ttk.Scale(master.frame_right,from_ = 100, to = 0, orient = VERTICAL, style="TScale", command = slider2_changed, variable = current_value2)
slider_6.grid(row=1, column=0,pady=0, padx=165, sticky="w")

# Value label
value_label2 = ttk.Label(master.frame_right,text=get_current_value2(), background = "gray18", justify="center", foreground="white")
value_label2.grid(row=1,column = 0, pady=0, padx=205,sticky='w')






## CONFIGURE THE SECOND FRAME FOR THE STRETCHER

#configure grid layout (3x7)
master.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
master.frame_right.rowconfigure(7, weight=10)
master.frame_right.columnconfigure((0, 1), weight=1)
master.frame_right.columnconfigure(2, weight=0)

## INPUT FILE 1

master.label_1 = customtkinter.CTkLabel(master=master.frame_right,text="File1:",text_font=("Roboto Medium", -16), fg_color=("white", "gray30"), width = 30)  # font name and size in px
master.label_1.grid(row=0, column=0, pady=5, padx=50, sticky="w")

master.frame_right.filelocation1 = customtkinter.CTkEntry(master=master.frame_right,width=10,placeholder_text="Path to the first input file")#TEXTBOX TO PRINT PATH OF THE SOUND FILE
master.frame_right.filelocation1.grid(row=0, column=0, columnspan=2, pady=5, padx=(120,200), sticky="we")
master.frame_right.filelocation1.focus_set()

# Button to browse the input file 1
open_file1 = customtkinter.CTkButton(master.frame_right, text="...", width = 3, command= browse_file1)
open_file1.grid(row=0, column=0, columnspan=2, sticky="e", padx=(150, 160), pady=5)

# Button to play the input file 1
#photo = PhotoImage(file= r"C:\Users\USUARIO\Desktop\play.jpg")
#photo = photo.subsample(14,14)
preview1 =customtkinter.CTkButton(master.frame_right, text="Play!",width = 3, command=lambda: UF.wavplay(master.frame_right.filelocation1.get()),fg_color=("gray75", "gray30"), hover_color = "green")
preview1.grid(row=0, column=0, columnspan = 3, sticky="e", padx=(250,100), pady=5)

##ANALYSIS WINDOW TYPE SOUND 1
#wtype1_label = "window1:"
#Label(master, text=wtype1_label).grid(row=1, column=0, sticky=W, padx=5, pady=(4,2))
#master.w1_type = StringVar()
#master.w1_type.set("hamming") # initial value
#window1_option = OptionMenu(master, master.w1_type, "rectangular", "hanning", "hamming", "blackman", "blackmanharris")
#window1_option.grid(row=1, column=0, sticky="W", padx=(68,5), pady=(4,2))
#
##WINDOW SIZE SOUND 1
#M1_label = "M1:"
#Label(master, text=M1_label).grid(row=1, column=0, sticky=W, padx=(180, 5), pady=(4,2))
#master.M1 = Entry(master, justify=CENTER)
#master.M1["width"] = 5
#master.M1.grid(row=1,column=0, sticky=W, padx=(208,5), pady=(4,2))
#master.M1.delete(0, END)
#master.M1.insert(0, "1024")
#
##FFT SIZE SOUND 1
#N1_label = "N1:"
#Label(master, text=N1_label).grid(row=1, column=0, sticky=W, padx=(265, 5), pady=(4,2))
#master.N1 = Entry(master, justify=CENTER)
#master.N1["width"] = 5
#master.N1.grid(row=1,column=0, sticky=W, padx=(290,5), pady=(4,2))
#master.N1.delete(0, END)
#master.N1.insert(0, "1024")
#
##HOP SIZE SOUND 1
#H1_label = "H1:"
#Label(master, text=H1_label).grid(row=1, column=0, sticky=W, padx=(343,5), pady=(4,2))
#master.H1 = Entry(master, justify=CENTER)
#master.H1["width"] = 5
#master.H1.grid(row=1, column=0, sticky=W, padx=(370,5), pady=(4,2))
#master.H1.delete(0, END)
#master.H1.insert(0, "256")
#
####
## SEPARATION LINE
#Frame(master, height=1, width=50, bg="black").grid(row=2, pady=15, sticky=W + E)
####
#
### INPUT FILE 2
#choose2_label = "inputFile2:"
#Label(master, text=choose2_label).grid(row=3, column=0, sticky=W, padx=5, pady=(2, 2))
#
## TEXTBOX TO PRINT PATH OF THE SOUND FILE
#master.filelocation2 = Entry(master)
#master.filelocation2.focus_set()
#master.filelocation2["width"] = 30
#master.filelocation2.grid(row=3, column=0, sticky=W, padx=(75, 5), pady=(2, 2))
#master.filelocation2.delete(0, END)
#
## BUTTON TO BROWSE SOUND FILE 2
#open_file2 = Button(master, text="...", command=browse_file2)  # see: def browse_file(self)
#open_file2.grid(row=3, column=0, sticky=W, padx=(330, 6), pady=(2, 2))  # put it beside the filelocation textbox
#
## BUTTON TO PREVIEW SOUND FILE 2
#preview2 = Button(master, text=">", command=lambda: UF.wavplay(master.filelocation2.get()), bg="gray30", fg="white")
#preview2.grid(row=3, column=0, sticky=W, padx=(375, 6), pady=(2, 2))
#
## ANALYSIS WINDOW TYPE SOUND 2
#wtype2_label = "window2:"
#Label(master, text=wtype2_label).grid(row=4, column=0, sticky=W, padx=5, pady=(4, 2))
#master.w2_type = StringVar()
#master.w2_type.set("hamming")  # initial value
#window2_option = OptionMenu(master, master.w2_type, "rectangular", "hanning", "hamming", "blackman","blackmanharris")
#window2_option.grid(row=4, column=0, sticky=W, padx=(68, 5), pady=(4, 2))
#
## WINDOW SIZE SOUND 2
#M2_label = "M2:"
#Label(master, text=M2_label).grid(row=4, column=0, sticky=W, padx=(180, 5), pady=(4, 2))
#master.M2 = Entry(master, justify=CENTER)
#master.M2["width"] = 5
#master.M2.grid(row=4, column=0, sticky=W, padx=(208, 5), pady=(4, 2))
#master.M2.delete(0, END)
#master.M2.insert(0, "1024")
#
## FFT SIZE SOUND 2
#N2_label = "N2:"
#Label(master, text=N2_label).grid(row=4, column=0, sticky=W, padx=(265, 5), pady=(4, 2))
#master.N2 = Entry(master, justify=CENTER)
#master.N2["width"] = 5
#master.N2.grid(row=4, column=0, sticky=W, padx=(290, 5), pady=(4, 2))
#master.N2.delete(0, END)
#master.N2.insert(0, "1024")
#
####
## SEPARATION LINE
#Frame(master, height=1, width=50, bg="black").grid(row=5, pady=15, sticky=W + E)
####
#
## SMOOTHING FACTOR
#smoothf_label1 = "Smooth factor of sound 2 (bigger than 0 to max of 1, where 1 is no"
#Label(master, text=smoothf_label1).grid(row=6, column=0, sticky=W, padx=(5, 5), pady=(2, 2))
#smoothf_label2 = "smothing):"
#Label(master, text=smoothf_label2).grid(row=7, column=0, sticky=W, padx=(5, 5), pady=(0, 2))
#master.smoothf = Entry(master, justify=CENTER)
#master.smoothf["width"] = 5
#master.smoothf.grid(row=8, column=0, sticky=W, padx=(5, 5), pady=(2, 2))
#master.smoothf.delete(0, END)
#master.smoothf.insert(0, "0.5")
#
## BALANCE FACTOR
#balancef_label = "Balance factor (from 0 to 1, where 0 is sound 1 and 1 is sound 2):"
#Label(master, text=balancef_label).grid(row=9, column=0, sticky=W, padx=(5, 5), pady=(10, 2))
#master.balancef = Entry(master, justify=CENTER)
#master.balancef["width"] = 5
#master.balancef.grid(row=10, column=0, sticky=W, padx=(5, 5), pady=(2, 2))
#master.balancef.delete(0, END)
#master.balancef.insert(0, "0.2")
#
## BUTTON TO DO THE SYNTHESIS
#compute = Button(master, text="Apply Transformation", command = transformation_synthesis, bg="dark green",fg="white")
#compute.grid(row=11, column=0, padx=5, pady=(10, 15), sticky=W)
#
## BUTTON TO PLAY TRANSFORMATION SYNTHESIS OUTPUT
#master.transf_output = Button(master, text=">", command=play_song, bg="gray30", fg="white")
#master.transf_output.grid(row=11, column=0, padx=(165, 5), pady=(10, 15), sticky=W)



## define options for opening file
#file_opt = options = {}
#options['defaultextension'] = '.wav'
#options['filetypes'] = [('All files', '.*'), ('Wav files', '.wav')]
#options['initialdir'] = '../../sounds/'
#options = 'Open a mono audio file .wav with sample frequency 44100 Hz'
#

master.mainloop()
