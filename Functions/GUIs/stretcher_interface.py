import os
import sys
from tkinter import *
import tkinter as tk
from tkinter import ttk
import customtkinter

from Functions import utilities as f

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../models/'))
from Functions.models import utilFunctions as UF


def stretcher_interface(master):

    ## CONFIGURE THE FRAME FOR THE STRETCHER

    # configure grid layout (3x7)
    master.stretcher_frame.rowconfigure((0, 1, 2, 3), weight=0)
    master.stretcher_frame.columnconfigure((0, 1), weight=1)
    master.stretcher_frame.columnconfigure(2, weight=0)

    ##TITLE
    master.label = customtkinter.CTkLabel(master=master.stretcher_frame,
                                          text="Stretcher", text_font=("Roboto Medium", -30),
                                          fg_color=("white", "gray18"), width=30)  # font name and size in px

    master.label.grid(row=0, column=0, pady=(15, 0), padx=40, sticky="w")

    ## INPUT FILE 1

    master.label_1 = customtkinter.CTkLabel(master=master.stretcher_frame,
                                            text="File1:",
                                            text_font=("Roboto Medium", -16),
                                            fg_color=("white", "gray30"),
                                            width=30)  # font name and size in px

    master.label_1.grid(row=1, column=0, pady=0, padx=50, sticky="w")

    master.stretcher_frame.filelocation1 = customtkinter.CTkEntry(master=master.stretcher_frame,
                                                                  width=10,
                                                                  placeholder_text="Path to the first input file")  # TEXTBOX TO PRINT PATH OF THE SOUND FILE

    master.stretcher_frame.filelocation1.grid(row=1, column=0, columnspan=2, pady=5, padx=(120, 200), sticky="we")
    master.stretcher_frame.filelocation1.focus_set()

    # Button to browse the input file 1
    open_file1 = customtkinter.CTkButton(master.stretcher_frame,
                                         text="...",
                                         width=3,
                                         command=lambda: f.browse_file1(master))

    open_file1.grid(row=1, column=0, columnspan=2, sticky="e", padx=(150, 160), pady=5)

    preview1 = customtkinter.CTkButton(master.stretcher_frame, text="Play!",
                                       width=3,
                                       command=lambda: UF.wavplay(master.stretcher_frame.filelocation1.get()),
                                       fg_color=("gray75", "gray30"),
                                       hover_color="green")

    preview1.grid(row=1, column=0, columnspan=3, sticky="e", padx=(250, 100), pady=5)

    ##DRAW THE AUDIO SPRECTOGRAM!!!

    master.to_do = customtkinter.CTkLabel(master=master.stretcher_frame,
                                          text="We need to implement something to show the audio during time",
                                          text_font=("Roboto Medium", -12),fg_color=("white", "gray18"), width=30)
    master.to_do.grid(row=3, column=0, columnspan=3, sticky="w", padx=(50, 300), pady=5)

    ##BUTTON FOR TIME DELAY
    # Create an slider space
    master.label_speed = customtkinter.CTkLabel(master=master.stretcher_frame,
                                                text="Speed",
                                                text_font=("Roboto Medium", -15),
                                                fg_color=("white", "gray30"),
                                                width=30)  # font name and size in px

    master.label_speed.grid(row=15, column=0, pady=(25, 0), padx=50, sticky="nw")

    # Define the style
    style = ttk.Style()
    style.configure("TScale", background="gray18")

    ##SLIDER
    # slider delay value
    master.speed_value = tk.DoubleVar()

    def slider15_changed(event):
        master.value360_label.configure(text='{: .2f}'.format(master.speed_value.get()))

    # Slider
    master.time_slider = ttk.Scale(master.stretcher_frame,
                              from_=0.5,
                              to=2.0,
                              length=450,
                              orient=HORIZONTAL,
                              style="TScale",
                              command=slider15_changed,
                              variable=master.speed_value)

    master.time_slider.grid(row=16, column=0, pady=20, padx=130, sticky="nw")

    # Right limit
    master.left_limit = customtkinter.CTkLabel(master=master.stretcher_frame,
                                                text="0.5",
                                                text_font=("Roboto Medium", -11),
                                                background="gray18",
                                                foreground="white")

    master.left_limit.grid(row=16, column=0, pady=(50, 0), padx=75, sticky="nw")

    # Left limit
    master.right_limit = customtkinter.CTkLabel(master=master.stretcher_frame,
                                               text="2.0",
                                               text_font=("Roboto Medium", -11),
                                               background="gray18",
                                               foreground="white")

    master.right_limit.grid(row=16, column=0, pady=(50, 0), padx=120, sticky="e")


    # VALUE LABEL
    master.label2 = customtkinter.CTkLabel(master=master.stretcher_frame,
                                           text="Value:",
                                           text_font=("Roboto Medium", -12),
                                           fg_color=("white", "gray30"),
                                           width=30)  # font name and size in px

    master.label2.grid(row=15, column=0, pady=(25, 0), padx=100, sticky="e")

    # VALUE NUMBER
    master.value360_label = ttk.Label(master.stretcher_frame,
                                   text="{:.2f}".format(master.speed_value.get()),                                   background="gray18",
                                   justify="center",
                                   foreground="white")

    master.value360_label.grid(row=15, column=0, pady=(25, 0), padx=60, sticky='e')

