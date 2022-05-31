import os
import sys
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

from Functions import utilities as f


sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../models/'))
from Functions.models import utilFunctions as UF


def stretcher_interface(master):

    ## CONFIGURE THE FRAME FOR THE STRETCHER

    # configure grid layout (3x7)
    master.stretcher_frame.rowconfigure(1, weight=0)


    ##TITLE
    master.stretcher_frame.frame_title = customtkinter.CTkLabel(master=master.stretcher_frame,
                                          text="Stretcher", text_font=("Roboto Medium", -30),
                                          fg_color=("white", "gray18"), width=30)  # font name and size in px

    master.stretcher_frame.frame_title.grid(row=0, column=0, pady=(15, 0), padx=40, sticky="w")

    ## INPUT FILE 1

    master.stretcher_frame.file_label = customtkinter.CTkLabel(master=master.stretcher_frame,
                                            text="File1:",
                                            text_font=("Roboto Medium", -16),
                                            fg_color=("white", "gray30"),
                                            width=30)  # font name and size in px

    master.stretcher_frame.file_label.grid(row=1, column=0, pady=0, padx=50, sticky="w")

    master.stretcher_frame.filelocation_stretcher = customtkinter.CTkEntry(master=master.stretcher_frame,
                                                                  width=10,
                                                                  placeholder_text="Path to the first input file")  # TEXTBOX TO PRINT PATH OF THE SOUND FILE

    master.stretcher_frame.filelocation_stretcher.grid(row=1, column=0, pady=20, padx=(120, 650), sticky="we")
    master.stretcher_frame.filelocation_stretcher.focus_set()

    # Button to browse the input file 1
    master.stretcher_frame.open_file_stretcher = customtkinter.CTkButton(master.stretcher_frame,
                                         text="...",
                                         width=3,
                                         command=lambda: f.browse_file1(master,2))

    master.stretcher_frame.open_file_stretcher.grid(row=1, column=0, sticky="e", padx=(70, 610), pady=5)

    master.stretcher_frame.preview_stretcher = customtkinter.CTkButton(master.stretcher_frame, text="Play!",
                                       width=3,
                                       command=lambda: UF.wavplay(master.stretcher_frame.filelocation_stretcher.get()),
                                       fg_color=("gray75", "gray30"),
                                       hover_color="green")

    master.stretcher_frame.preview_stretcher.grid(row=1, column=0, columnspan=3, sticky="e", padx=(150, 550), pady=20)

    #Draw the audio plot
    fig3 = Figure(figsize=(16,9), dpi = 100)
    fig3.set_facecolor('#2e2e2e')
    a3= fig3.add_subplot(111)
    data = np.random.uniform(-1,1,44100)
    a3.plot(data)
    a3.axis('off')
    canvas3 = FigureCanvasTkAgg(fig3, master.stretcher_frame)
    canvas3.draw()
    canvas3.get_tk_widget().configure(background='black', width=720, height=200)
    canvas3.get_tk_widget().grid(row=2, column=0, sticky="w", padx=(20, 580), pady=(0,0))


    # Define the style
    style = ttk.Style()
    style.configure("TScale", background="gray18")

    ##BUTTON FOR TIME DELAY

    # Create an slider space
    master.stretcher_frame.label_speed = customtkinter.CTkLabel(master=master.stretcher_frame,
                                                text="Speed",
                                                text_font=("Roboto Medium", -15),
                                                fg_color=("white", "gray30"),
                                                width=30)  # font name and size in px

    master.stretcher_frame.label_speed.grid(row=3, column=0, pady=(25, 0), padx=50, sticky="nw")

    ##SLIDER
    # slider delay value
    master.stretcher_frame.speed_value = tk.DoubleVar()

    def slider15_changed(event):
        master.stretcher_frame.value_number.configure(text='{: .2f}'.format(master.stretcher_frame.speed_value.get()))

    # Slider
    master.stretcher_frame.time_slider = ttk.Scale(master.stretcher_frame,
                              from_=0.5,
                              to=2.0,
                              length=450,
                              orient=HORIZONTAL,
                              style="TScale",
                              command=slider15_changed,
                              variable=master.stretcher_frame.speed_value)

    master.stretcher_frame.time_slider.grid(row=4, column=0, pady=20, padx=130, sticky="nw")

    # Left limit
    master.stretcher_frame.left_limit_stretcher = customtkinter.CTkLabel(master=master.stretcher_frame,
                                                text="0.5",
                                                text_font=("Roboto Medium", -11),
                                                background="gray18",
                                                foreground="white")

    master.stretcher_frame.left_limit_stretcher.grid(row=4, column=0, pady=(50, 0), padx=75, sticky="nw")

    # Right limit
    master.stretcher_frame.right_limit_stretcher = customtkinter.CTkLabel(master=master.stretcher_frame,
                                               text="2.0",
                                               text_font=("Roboto Medium", -11),
                                               background="gray18",
                                               foreground="white")

    master.stretcher_frame.right_limit_stretcher.grid(row=4, column=0, pady=(50, 0), padx=530, sticky="w")


    # VALUE LABEL
    master.stretcher_frame.value_label = customtkinter.CTkLabel(master=master.stretcher_frame,
                                           text="Value:",
                                           text_font=("Roboto Medium", -12),
                                           fg_color=("white", "gray30"),
                                           width=30)  # font name and size in px

    master.stretcher_frame.value_label.grid(row=3, column=0, pady=(25, 0), padx=580, sticky="sw")

    # VALUE NUMBER
    master.stretcher_frame.value_number = ttk.Label(master.stretcher_frame,
                                   text="{:.2f}".format(master.stretcher_frame.speed_value.get()),
                                   background="gray18",
                                   justify="center",
                                   foreground="white")

    master.stretcher_frame.value_number.grid(row=3, column=0, pady=(25, 0), padx=0, sticky='s')

    master.stretcher_frame.time_slider.set(1)
