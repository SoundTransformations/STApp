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
    master.equalizer_frame.rowconfigure(1, weight=0)


    master.label = customtkinter.CTkLabel(master=master.equalizer_frame,
                                            text="Equalizer",
                                            text_font=("Roboto Medium", -30),
                                            fg_color=("white", "gray18"),
                                            width=30)  # font name and size in px

    master.label.grid(row=0, column=0, pady=(15,0), padx=40, sticky="w")


    ## INPUT FILE 1
    master.label_1 = customtkinter.CTkLabel(master=master.equalizer_frame,
                                            text="File1:",
                                            text_font=("Roboto Medium", -16),
                                            fg_color=("white", "gray30"),
                                            width=30)  # font name and size in px

    master.label_1.grid(row=1, column=0, pady=0, padx=50, sticky="w")

    master.equalizer_frame.filelocation1 = customtkinter.CTkEntry(master=master.equalizer_frame,
                                                                  width=10,
                                                                  placeholder_text="Path to the first input file")  # TEXTBOX TO PRINT PATH OF THE SOUND FILE

    master.equalizer_frame.filelocation1.grid(row=1, column=0, pady=20, padx=(120, 480), sticky="we")
    master.equalizer_frame.filelocation1.focus_set()

    # Button to browse the input file 1
    open_file1 = customtkinter.CTkButton(master.equalizer_frame,
                                         text="...", width=3,
                                         command=lambda: f.browse_file1(master))

    open_file1.grid(row=1, column=0, sticky="e", padx=(70, 440), pady=5)

    # Button to play the input file 1
    preview1 = customtkinter.CTkButton(master.equalizer_frame,
                                       text="Play!", width=3,
                                       command=lambda: UF.wavplay(master.equalizer_frame.filelocation1.get()),
                                       fg_color=("gray75", "gray30"),
                                       hover_color="green")

    preview1.grid(row=1, column=0, columnspan=3, sticky="e", padx=(250, 380), pady=20)

    # SLIDERS of the EQUALIZER

    # Define the style
    style = ttk.Style()
    style.configure("TScale", background="gray18")


    # Create an slider space

    master.label_6 = customtkinter.CTkLabel(master=master.equalizer_frame,
                                            text="32 Hz",
                                            text_font=("Roboto Medium", -12),
                                            fg_color=("white", "gray30"),
                                            width=30)  # font name and size in px

    master.label_6.grid(row=2, column=0, pady=(15,0), padx=50, sticky="nw")

    # slider current value
    master.current_value1 = tk.DoubleVar()

    def slider1_changed(event):
        master.value_label1.configure(text='{: .2f}'.format(master.current_value1.get()))

    # Slider
    master.slider_5 = ttk.Scale(master.equalizer_frame,
                                from_=100,
                                to=0,
                                orient=VERTICAL,
                                style="TScale",
                                command= slider1_changed,
                                variable=master.current_value1)

    master.slider_5.grid(row=3, column=0, pady=10, padx=65, sticky="w")

    # Value label
    master.value_label1 = ttk.Label(master.equalizer_frame,
                                    text='{: .2f}'.format(master.current_value1.get()),
                                    background="gray18",
                                    justify="center",
                                    foreground="white")

    master.value_label1.grid(row=4, column=0, pady=0, padx=61, sticky='sw')


    ## Create an slider space

    master.label_7 = customtkinter.CTkLabel(master=master.equalizer_frame,
                                            text="64 Hz",
                                            text_font=("Roboto Medium", -12),
                                            fg_color=("white", "gray30"),
                                            width=30)

    master.label_7.grid(row=2, column=0, pady=(15,0), padx=110, sticky="nw")

    # Slider current value
    master.current_value2 = tk.DoubleVar()

    def slider2_changed(event):
        master.value_label2.configure(text='{: .2f}'.format(master.current_value2.get()))

    # Slider
    master.slider_6 = ttk.Scale(master.equalizer_frame,
                                from_=100,
                                to=0,
                                orient=VERTICAL,
                                style="TScale",
                                command= slider2_changed,
                                variable=master.current_value2)

    master.slider_6.grid(row=3, column=0, pady=10, padx=122, sticky="w")

    # Value label
    master.value_label2 = ttk.Label(master.equalizer_frame,
                                    text='{: .2f}'.format(master.current_value2.get()),
                                    background="gray18",
                                    justify="center",
                                    foreground="white")

    master.value_label2.grid(row=4, column=0, pady=0, padx=119, sticky='sw')

    ## Create an slider space

    master.label_7 = customtkinter.CTkLabel(master=master.equalizer_frame,
                                            text="125 Hz",
                                            text_font=("Roboto Medium", -12),
                                            fg_color=("white", "gray30"),
                                            width=30)

    master.label_7.grid(row=2, column=0, pady=(15,0), padx=170, sticky="nw")

    # Slider current value
    master.current_value3 = tk.DoubleVar()

    def slider3_changed(event):
        master.value_label3.configure(text='{: .2f}'.format(master.current_value3.get()))

    # Slider
    master.slider_7 = ttk.Scale(master.equalizer_frame,
                                from_=100,
                                to=0,
                                orient=VERTICAL,
                                style="TScale",
                                command=slider3_changed,
                                variable=master.current_value3)

    master.slider_7.grid(row=3, column=0, pady=10, padx=185, sticky="w")

    # Value label
    master.value_label3 = ttk.Label(master.equalizer_frame,
                                    text='{: .2f}'.format(master.current_value3.get()),
                                    background="gray18",
                                    justify="center",
                                    foreground="white")

    master.value_label3.grid(row=4, column=0, pady=0, padx=181, sticky='sw')

    ## Create an slider space

    master.label_8 = customtkinter.CTkLabel(master=master.equalizer_frame,
                                            text="260 Hz",
                                            text_font=("Roboto Medium", -12),
                                            fg_color=("white", "gray30"),
                                            width=30)

    master.label_8.grid(row=2, column=0, pady=(15,0), padx=238, sticky="nw")

    # Slider current value
    master.current_value4 = tk.DoubleVar()

    def slider4_changed(event):
        master.value_label4.configure(text='{: .2f}'.format(master.current_value4.get()))

    # Slider
    master.slider_8 = ttk.Scale(master.equalizer_frame,
                                from_=100,
                                to=0,
                                orient=VERTICAL,
                                style="TScale",
                                command=slider4_changed,
                                variable=master.current_value4)

    master.slider_8.grid(row=3, column=0, pady=10, padx=250, sticky="w")

    # Value label
    master.value_label4 = ttk.Label(master.equalizer_frame,
                                    text='{: .2f}'.format(master.current_value4.get()),
                                    background="gray18",
                                    justify="center",
                                    foreground="white")

    master.value_label4.grid(row=4, column=0, pady=0, padx= 246, sticky='sw')

    ## Create an slider space

    master.label_15 = customtkinter.CTkLabel(master=master.equalizer_frame,
                                            text="500 Hz",
                                            text_font=("Roboto Medium", -12),
                                            fg_color=("white", "gray30"),
                                            width=30)

    master.label_15.grid(row=2, column=0, pady=(15,0), padx= 305, sticky="nw")

    # Slider current value
    master.current_value15 = tk.DoubleVar()

    def slider15_changed(event):
        master.value_label15.configure(text='{: .2f}'.format(master.current_value15.get()))

    # Slider
    master.slider_15 = ttk.Scale(master.equalizer_frame,
                                from_=100,
                                to=0,
                                orient=VERTICAL,
                                style="TScale",
                                command=slider15_changed,
                                variable=master.current_value15)

    master.slider_15.grid(row=3, column=0, pady=10, padx=320, sticky="w")

    # Value label
    master.value_label15 = ttk.Label(master.equalizer_frame,
                                    text='{: .2f}'.format(master.current_value15.get()),
                                    background="gray18",
                                    justify="center",
                                    foreground="white")

    master.value_label15.grid(row=4, column=0, pady=0, padx=315, sticky='sw')


    ## Create an slider space

    master.label_10 = customtkinter.CTkLabel(master=master.equalizer_frame,
                                            text="1k Hz",
                                            text_font=("Roboto Medium", -12),
                                            fg_color=("white", "gray30"),
                                            width=30)

    master.label_10.grid(row=2, column=0, pady=(15,0), padx=372, sticky="nw")

    # Slider current value
    master.current_value5 = tk.DoubleVar()

    def slider5_changed(event):
        master.value_label5.configure(text='{: .2f}'.format(master.current_value5.get()))

    # Slider
    master.slider_9 = ttk.Scale(master.equalizer_frame,
                                from_=100,
                                to=0,
                                orient=VERTICAL,
                                style="TScale",
                                command=slider5_changed,
                                variable=master.current_value5)

    master.slider_9.grid(row=3, column=0, pady=10, padx=382, sticky="w")

    # Value label
    master.value_label5 = ttk.Label(master.equalizer_frame,
                                    text='{: .2f}'.format(master.current_value5.get()),
                                    background="gray18",
                                    justify="center",
                                    foreground="white")

    master.value_label5.grid(row=4, column=0, pady=0, padx=378, sticky='sw')

    ## Create an slider space

    master.label_11 = customtkinter.CTkLabel(master=master.equalizer_frame,
                                             text="2k Hz",
                                             text_font=("Roboto Medium", -12),
                                             fg_color=("white", "gray30"),
                                             width=30)

    master.label_11.grid(row=2, column=0, pady=(15,0), padx=430, sticky="nw")

    # Slider current value
    master.current_value6 = tk.DoubleVar()

    def slider6_changed(event):
        master.value_label6.configure(text='{: .2f}'.format(master.current_value6.get()))

    # Slider
    master.slider_10 = ttk.Scale(master.equalizer_frame,
                                from_=100,
                                to=0,
                                orient=VERTICAL,
                                style="TScale",
                                command=slider6_changed,
                                variable=master.current_value6)

    master.slider_10.grid(row=3, column=0, pady=10, padx=442, sticky="w")

    # Value label
    master.value_label6 = ttk.Label(master.equalizer_frame,
                                    text='{: .2f}'.format(master.current_value6.get()),
                                    background="gray18",
                                    justify="center",
                                    foreground="white")

    master.value_label6.grid(row=4, column=0, pady=0, padx=438, sticky='sw')

    ## Create an slider space

    master.label_12 = customtkinter.CTkLabel(master=master.equalizer_frame,
                                             text="4k Hz",
                                             text_font=("Roboto Medium", -12),
                                             fg_color=("white", "gray30"),
                                             width=30)

    master.label_12.grid(row=2, column=0, pady=(15,0), padx=490, sticky="nw")

    # Slider current value
    master.current_value7 = tk.DoubleVar()

    def slider7_changed(event):
        master.value_label7.configure(text='{: .2f}'.format(master.current_value7.get()))

    # Slider
    master.slider_11 = ttk.Scale(master.equalizer_frame,
                                 from_=100,
                                 to=0,
                                 orient=VERTICAL,
                                 style="TScale",
                                 command=slider7_changed,
                                 variable=master.current_value7)

    master.slider_11.grid(row=3, column=0, pady=10, padx=500, sticky="w")

    # Value label
    master.value_label7 = ttk.Label(master.equalizer_frame,
                                    text='{: .2f}'.format(master.current_value7.get()),
                                    background="gray18",
                                    justify="center",
                                    foreground="white")

    master.value_label7.grid(row=4, column=0, pady=0, padx=498, sticky='sw')

    ## Create an slider space

    master.label_13 = customtkinter.CTkLabel(master=master.equalizer_frame,
                                             text="8k Hz",
                                             text_font=("Roboto Medium", -12),
                                             fg_color=("white", "gray30"),
                                             width=30)

    master.label_13.grid(row=2, column=0, pady=(15,0), padx=550, sticky="n")

    # Slider current value
    master.current_value8 = tk.DoubleVar()

    def slider8_changed(event):
        master.value_label8.configure(text='{: .2f}'.format(master.current_value8.get()))

    # Slider
    master.slider_12 = ttk.Scale(master.equalizer_frame,
                                 from_=100,
                                 to=0,
                                 orient=VERTICAL,
                                 style="TScale",
                                 command=slider8_changed,
                                 variable=master.current_value8)

    master.slider_12.grid(row=3, column=0, pady=10, padx=562, sticky="w")

    # Value label
    master.value_label8 = ttk.Label(master.equalizer_frame,
                                    text='{: .2f}'.format(master.current_value8.get()),
                                    background="gray18",
                                    justify="center",
                                    foreground="white")

    master.value_label8.grid(row=4, column=0, pady=0, padx=558, sticky='sw')

    ## Create an slider space

    master.label_14 = customtkinter.CTkLabel(master=master.equalizer_frame,
                                             text="16k Hz",
                                             text_font=("Roboto Medium", -12),
                                             fg_color=("white", "gray30"),
                                             width=30)

    master.label_14.grid(row=2, column=0, pady=(15,0), padx=485, sticky="ne")

    # Slider current value
    master.current_value9 = tk.DoubleVar()

    def slider9_changed(event):
        master.value_label9.configure(text='{: .2f}'.format(master.current_value9.get()))

    # Slider
    master.slider_13 = ttk.Scale(master.equalizer_frame,
                                 from_=100,
                                 to=0,
                                 orient=VERTICAL,
                                 style="TScale",
                                 command=slider9_changed,
                                 variable=master.current_value9)

    master.slider_13.grid(row=3, column=0, pady=10, padx=502, sticky="e")

    # Value label
    master.value_label9 = ttk.Label(master.equalizer_frame,
                                    text='{: .2f}'.format(master.current_value9.get()),
                                    background="gray18",
                                    justify="center",
                                    foreground="white")

    master.value_label9.grid(row=4, column=0, pady=0, padx=502, sticky='se')

