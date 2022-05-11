import os
import sys
from tkinter import *
import tkinter as tk
from tkinter import ttk
import customtkinter

from Functions import utilities as f

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../models/'))
from Functions.models import utilFunctions as UF


def equalizer_interface(master):

    ## CONFIGURE THE EQUALIZER FRAME

    # Configure grid layout (3x7)
    master.equalizer_frame.rowconfigure((0, 1, 2, 3), weight=1)
    master.equalizer_frame.rowconfigure(7, weight=10)
    master.equalizer_frame.columnconfigure((0, 1), weight=1)
    master.equalizer_frame.columnconfigure(2, weight=0)

    ## INPUT FILE 1
    master.label_1 = customtkinter.CTkLabel(master=master.equalizer_frame,
                                            text="File1:",
                                            text_font=("Roboto Medium", -16),
                                            fg_color=("white", "gray30"),
                                            width=30)  # font name and size in px

    master.label_1.grid(row=0, column=0, pady=5, padx=50, sticky="w")

    master.equalizer_frame.filelocation1 = customtkinter.CTkEntry(master=master.equalizer_frame,
                                                                  width=10,
                                                                  placeholder_text="Path to the first input file")  # TEXTBOX TO PRINT PATH OF THE SOUND FILE

    master.equalizer_frame.filelocation1.grid(row=0, column=0, columnspan=2, pady=5, padx=(120, 200), sticky="we")
    master.equalizer_frame.filelocation1.focus_set()

    # Button to browse the input file 1
    open_file1 = customtkinter.CTkButton(master.equalizer_frame,
                                         text="...", width=3,
                                         command=lambda: f.browse_file1(master))

    open_file1.grid(row=0, column=0, columnspan=2, sticky="e", padx=(150, 160), pady=5)

    # Button to play the input file 1
    preview1 = customtkinter.CTkButton(master.equalizer_frame,
                                       text="Play!", width=3,
                                       command=lambda: UF.wavplay(master.equalizer_frame.filelocation1.get()),
                                       fg_color=("gray75", "gray30"),
                                       hover_color="green")

    preview1.grid(row=0, column=0, columnspan=3, sticky="e", padx=(250, 100), pady=5)

    # SLIDERS of the EQUALIZER
    style = ttk.Style()
    style.configure("TScale", background="gray18")

    master.label_6 = customtkinter.CTkLabel(master=master.equalizer_frame,
                                            text="30 Hz",
                                            text_font=("Roboto Medium", -12),
                                            fg_color=("white", "gray30"),
                                            width=30)  # font name and size in px

    master.label_6.grid(row=2, column=0, pady=0, padx=50, sticky="w")


    # slider current value
    master.current_value1 = tk.DoubleVar()

    def slider1_changed(event):
        master.value_label1.configure(text='{: .2f}'.format(master.current_value1.get()))



    master.slider_5 = ttk.Scale(master.equalizer_frame,
                                from_=100,
                                to=0,
                                orient=VERTICAL,
                                style="TScale",
                                command= slider1_changed,
                                variable=master.current_value1)

    master.slider_5.grid(row=1, column=0, pady=0, padx=65, sticky="w")

    # Value label
    master.value_label1 = ttk.Label(master.equalizer_frame,
                                    text='{: .2f}'.format(master.current_value1.get()),
                                    background="gray18",
                                    justify="center",
                                    foreground="white")

    master.value_label1.grid(row=1, column=0, pady=0, padx=105, sticky='w')

    master.label_7 = customtkinter.CTkLabel(master=master.equalizer_frame,
                                            text="60 Hz",
                                            text_font=("Roboto Medium", -12),
                                            fg_color=("white", "gray30"),
                                            width=30)

    master.label_7.grid(row=2, column=0, pady=0, padx=150, sticky="w")

    def slider2_changed(event):
        master.value_label2.configure(text='{: .2f}'.format(master.current_value2.get()))

    # slider current value
    master.current_value2 = tk.DoubleVar()

    master.slider_6 = ttk.Scale(master.equalizer_frame,
                                from_=100,
                                to=0,
                                orient=VERTICAL,
                                style="TScale",
                                command= slider2_changed,
                                variable=master.current_value2)

    master.slider_6.grid(row=1, column=0, pady=0, padx=165, sticky="w")

    # Value label
    master.value_label2 = ttk.Label(master.equalizer_frame,
                                    text='{: .2f}'.format(master.current_value2.get()),
                                    background="gray18",
                                    justify="center",
                                    foreground="white")

    master.value_label2.grid(row=1, column=0, pady=0, padx=205, sticky='w')