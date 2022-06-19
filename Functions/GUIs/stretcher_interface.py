from tkinter import *
import tkinter as tk
from tkinter import ttk
import customtkinter

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

from Functions import utilities as f

def stretcher_interface(master):

    ## CONFIGURE THE FRAME FOR THE STRETCHER

    # configure grid layout (3x7)
    master.stretcher_frame.rowconfigure(1, weight=0)


    ##TITLE
    master.stretcher_frame.frame_title = customtkinter.CTkLabel(master=master.stretcher_frame,
                                          text="Time Stretcher", text_font=("Roboto Medium", -30),
                                          fg_color=("white", "gray18"), width=30)  # font name and size in px

    master.stretcher_frame.frame_title.grid(row=0, column=0, pady=(15, 0), padx=40, sticky="w")

    ## INPUT FILE 1

    master.stretcher_frame.file_label = customtkinter.CTkLabel(master=master.stretcher_frame,
                                            text="File:",
                                            text_font=("Roboto Medium", -16),
                                            fg_color=("white", "gray30"),
                                            width=30)  # font name and size in px

    master.stretcher_frame.file_label.grid(row=1, column=0, pady=0, padx=50, sticky="w")

    master.stretcher_frame.filelocation_stretcher = customtkinter.CTkEntry(master=master.stretcher_frame,
                                                                  width=10,
                                                                  placeholder_text="Path to the file: 16 bits, mono and 44100 Hz of sampling rate!")  # TEXTBOX TO PRINT PATH OF THE SOUND FILE

    master.stretcher_frame.filelocation_stretcher.grid(row=1, column=0, pady=20, padx=(110, 650), sticky="we")
    master.stretcher_frame.filelocation_stretcher.focus_set()

    # Button to browse the input file 1
    master.stretcher_frame.open_file_stretcher = customtkinter.CTkButton(master.stretcher_frame,
                                         text="Import",
                                         width=3,
                                         command=lambda: f.browse_file1(master,2))

    master.stretcher_frame.open_file_stretcher.grid(row=1, column=0, sticky="e", padx=(70, 580), pady=5)

    #Draw the audio plot
    fig3 = Figure(figsize=(16,9), dpi = 100)
    fig3.set_facecolor('#2e2e2e')
    a3= fig3.add_subplot(111)
    data = np.zeros(2)
    a3.plot(data)
    a3.axis('off')
    canvas3 = FigureCanvasTkAgg(fig3, master.stretcher_frame)
    canvas3.draw()
    canvas3.get_tk_widget().configure(background='black', width=720, height=200)
    canvas3.get_tk_widget().grid(row=2, column=0, sticky="w", padx=(20, 580), pady=(0,0))

    master.stretcher_frame.no_audio_label = customtkinter.CTkLabel(master=master.stretcher_frame,
                                                                   text="No audio loaded",
                                                                   text_font=("Roboto Medium", -15),
                                                                   fg_color=("white", "gray18"),
                                                                   width=30)  # font name and size in px

    master.stretcher_frame.no_audio_label.grid(row=2, column=0, pady=(50, 0), padx=(325, 600), sticky="w")



    # Define the style
    style = ttk.Style()
    style.configure("TScale", background="gray18")

    ##BUTTON FOR TIME DELAY

    # Create an slider space
    master.stretcher_frame.label_speed = customtkinter.CTkLabel(master=master.stretcher_frame,
                                                text="Stretch factor",
                                                text_font=("Roboto Medium", -15),
                                                fg_color=("white", "gray30"),
                                                width=30)  # font name and size in px

    master.stretcher_frame.label_speed.grid(row=3, column=0, pady=(23, 0), padx=35, sticky="nw")

    # Button to reset the slider
    master.stretcher_frame.btn_reset_stretcher_slider = customtkinter.CTkButton(master.stretcher_frame,
                                                                        text="R",
                                                                        width=1,
                                                                        text_font=("Roboto Medium", -9),
                                                                        height=1,
                                                                        fg_color="gray40",
                                                                        command=lambda: [f.reset_slider_stretcher(master),f.stretching(master, 2, master.stretcher_frame.filelocation_stretcher.get())])

    master.stretcher_frame.btn_reset_stretcher_slider.grid(row=3, column=0, pady=(27, 0), padx=157, sticky='nw')

    ##SLIDER
    # slider delay value
    master.stretcher_frame.speed_value = tk.DoubleVar()

    def slider15_changed(event):
        master.stretcher_frame.value_number.configure(text='{: .2f}'.format(master.stretcher_frame.speed_value.get()))

    # Slider
    master.stretcher_frame.time_slider = ttk.Scale(master.stretcher_frame,
                              from_=0.5,
                              to=2.0,
                              length=410,
                              orient=HORIZONTAL,
                              style="TScale",
                              command=slider15_changed,
                              variable=master.stretcher_frame.speed_value)

    master.stretcher_frame.time_slider.grid(row=3, column=0, pady=(23,0), padx=200, sticky="nw")

    master.stretcher_frame.time_slider.bind("<ButtonRelease-1>",
                                         lambda h: f.stretching(master, 2, master.stretcher_frame.filelocation_stretcher.get()))

    # Left limit
    master.stretcher_frame.left_limit_stretcher = customtkinter.CTkLabel(master=master.stretcher_frame,
                                                text="x2",
                                                text_font=("Roboto Medium", -11),
                                                background="gray18",
                                                foreground="white")

    master.stretcher_frame.left_limit_stretcher.grid(row=3, column=0, pady=(45, 0), padx=150, sticky="nw")

    # Right limit
    master.stretcher_frame.right_limit_stretcher = customtkinter.CTkLabel(master=master.stretcher_frame,
                                               text="x0.5",
                                               text_font=("Roboto Medium", -11),
                                               background="gray18",
                                               foreground="white")

    master.stretcher_frame.right_limit_stretcher.grid(row=3, column=0, pady=(45, 0), padx=535, sticky="nw")

    # VALUE NUMBER
    master.stretcher_frame.value_number = ttk.Label(master.stretcher_frame,
                                   text="{:.2f}".format(master.stretcher_frame.speed_value.get()),
                                   background="gray18",
                                   justify="center",
                                   foreground="white")

    master.stretcher_frame.value_number.grid(row=3, column=0, pady=(60,0), padx=389, sticky='w')

    master.stretcher_frame.time_slider.set(1)

    # Forward the slider
    master.stretcher_frame.forward_slider = customtkinter.CTkButton(master.stretcher_frame,
                                                                  text=">", width=1,height=1,
                                                                  command=lambda: [f.forward_stretcher_slider(master),f.stretching(master, 2, master.stretcher_frame.filelocation_stretcher.get())],
                                                                  fg_color=("gray75", "gray30"))

    master.stretcher_frame.forward_slider.grid(row=3, column=0, pady=(60,0), padx=460, sticky='w')

    # Backward the slider
    master.stretcher_frame.backward_slider = customtkinter.CTkButton(master.stretcher_frame,
                                                                    text="<", width=1, height=1,
                                                                    command=lambda:[f.backward_stretcher_slider(master),f.stretching(master, 2, master.stretcher_frame.filelocation_stretcher.get())],
                                                                    fg_color=("gray75", "gray30"))

    master.stretcher_frame.backward_slider.grid(row=3, column=0, pady=(60,0), padx=319, sticky='w')


    # Button to save the result
    master.stretcher_frame.save_button = customtkinter.CTkButton(master.stretcher_frame,
                                                             text="Save", width=3,
                                                             command=lambda: f.save_audio(master.y2, 44100),
                                                             fg_color=("gray75", "gray30"),
                                                             state=DISABLED)

    master.stretcher_frame.save_button.grid(row=3, column=0, sticky="ne", padx=(70, 595), pady=0)

    # Button to play the result
    master.stretcher_frame.play_result_button = customtkinter.CTkButton(master.stretcher_frame,
                                                                    text="▶", width=3,
                                                                    command=lambda: f.play_song(master.y2, 44100),
                                                                    fg_color=("gray75", "gray30"))

    master.stretcher_frame.play_result_button.grid(row=3, column=0, sticky="ne", padx=(100, 585), pady=40)

    # Button to stop the result
    master.stretcher_frame.stop_result_button = customtkinter.CTkButton(master.stretcher_frame,
                                                                    text="II", width=3,
                                                                    command=lambda: f.stop_song(master.y2),
                                                                    fg_color=("gray75", "gray30"))

    master.stretcher_frame.stop_result_button.grid(row=3, column=0, sticky="ne", padx=(100, 625), pady=40)
