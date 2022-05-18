import os
import sys
from tkinter import *
import tkinter as tk
from tkinter import ttk
import customtkinter

from Functions import utilities as f

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../models/'))
from Functions.models import utilFunctions as UF


def create_other_interface(master):
    ## CONFIGURE THE PITCH SHIFTING FRAME

    # Configure grid layout (3x7)
    master.other_interface.rowconfigure(1, weight=0)

    master.label = customtkinter.CTkLabel(master=master.other_interface,
                                          text="Pitch shifting",
                                          text_font=("Roboto Medium", -30),
                                          fg_color=("white", "gray18"),
                                          width=30)  # font name and size in px

    master.label.grid(row=0, column=0, pady=(15, 0), padx=40, sticky="w")

    ## INPUT FILE 1
    master.label_1 = customtkinter.CTkLabel(master=master.other_interface,
                                            text="File1:",
                                            text_font=("Roboto Medium", -16),
                                            fg_color=("white", "gray30"),
                                            width=30)  # font name and size in px

    master.label_1.grid(row=1, column=0, pady=0, padx=50, sticky="w")

    master.other_interface.filelocation1 = customtkinter.CTkEntry(master=master.other_interface,
                                                                  width=550,
                                                                  placeholder_text="Path to the first input file")  # TEXTBOX TO PRINT PATH OF THE SOUND FILE

    master.other_interface.filelocation1.grid(row=1, column=0, pady=20, padx=(120, 480), sticky="nw")
    master.other_interface.filelocation1.focus_set()

    # Button to browse the input file 1
    open_file1 = customtkinter.CTkButton(master.other_interface,
                                         text="...", width=3,
                                         command=lambda: f.browse_file1(master))

    open_file1.grid(row=1, column=0, sticky="n", padx=(0, 95), pady=20)

    # Button to play the input file 1
    preview1 = customtkinter.CTkButton(master.other_interface,
                                       text="Play!", width=3,
                                       command=lambda: UF.wavplay(master.other_interface.filelocation1.get()),
                                       fg_color=("gray75", "gray30"),
                                       hover_color="green")

    preview1.grid(row=1, column=0, columnspan=3, sticky="n", padx=(0, 3), pady=20)

    # Define the style
    style = ttk.Style()
    style.configure("TScale", background="gray18")


    # Create an slider space
    master.label_pitch = customtkinter.CTkLabel(master=master.other_interface,
                                            text="Tone scale",
                                            text_font=("Roboto Medium", -15),
                                            fg_color=("white", "gray30"),
                                            width=30)  # font name and size in px

    master.label_pitch.grid(row=2, column=0, pady=(25, 0), padx=50, sticky="nw")

    # slider current value
    master.current_value = tk.DoubleVar()

    def slider_changed(event):
        master.value_label.configure(text='{: .2f}'.format(master.current_value.get()))

    # Slider
    master.slider = ttk.Scale(master.other_interface,
                                from_=-2400,
                                to=2400,
                                length = 450,
                                orient=HORIZONTAL,
                                style="TScale",
                                command=slider_changed,
                                variable=master.current_value)

    master.slider.grid(row=2, column=0, pady=25, padx=170, sticky="w")

    # Right limit
    master.right_limit = customtkinter.CTkLabel(master=master.other_interface,
                                                text="-2400",
                                                text_font=("Roboto Medium", -11),
                                                background="gray18",
                                                foreground="white")

    master.right_limit.grid(row=2, column=0, pady=(50, 0), padx=120, sticky="nw")

    # Left limit
    master.left_limit = customtkinter.CTkLabel(master=master.other_interface,
                                                text="2400",
                                                text_font=("Roboto Medium", -11),
                                                background="gray18",
                                                foreground="white")

    master.left_limit.grid(row=2, column=0, pady=(50, 0), padx=560, sticky="nw")

    # Second label
    master.label2 = customtkinter.CTkLabel(master=master.other_interface,
                                           text="Value:",
                                           text_font=("Roboto Medium", -12),
                                           fg_color=("white", "gray30"),
                                           width=30)  # font name and size in px

    master.label2.grid(row=2, column=0, pady=(25, 0), padx=670, sticky="nw")

    # Value label
    master.value_label = ttk.Label(master.other_interface,
                                   text='{: .2f}'.format(master.current_value.get()),
                                   background="gray18",
                                   justify="center",
                                   foreground="white")

    master.value_label.grid(row=2, column=0, pady=(25, 0), padx=730, sticky='nw')


