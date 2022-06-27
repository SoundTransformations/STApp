import customtkinter
from Functions import utilities as f

import os
import sys
import tkinter as tk

def create_main_interface(master):

    # Create the Menu Selector Frame
    master.frame_left = customtkinter.CTkFrame(master=master, width=180, corner_radius=0)
    master.frame_left.grid(row=0, column=0, sticky="nswe")

    # Create a test frame

    master.pitch_frame = customtkinter.CTkFrame(master=master)
    master.pitch_frame.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

    # Create two possible frames (Equalizer and Stretcher)

    master.stretcher_frame = customtkinter.CTkFrame(master=master)
    master.stretcher_frame.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

    master.equalizer_frame = customtkinter.CTkFrame(master=master)
    master.equalizer_frame.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)



    # configure grid layout (1x11)
    master.frame_left.grid_rowconfigure(0, minsize=10)  # empty row with minsize as spacing
    master.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
    master.frame_left.grid_rowconfigure(8, minsize=20)  # empty row with minsize as spacing
    master.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

    def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    path = resource_path("STApp_logo.png")
    photo = tk.PhotoImage(file=path)

    master.label_1 = customtkinter.CTkButton(master=master.frame_left,
                                             text = '',
                                             fg_color='#2e2e2e',
                                             image = photo,
                                            compound='right',
                                             width = 100, height = 5)

    master.label_1.grid(row=1, column=0, pady=5, padx=0)

    # Add a button
    master.button_1 = customtkinter.CTkButton(master=master.frame_left,
                                              text="Equalizer",
                                              fg_color=("gray75", "gray30"),
                                              command=lambda: f.change_to_frame1(master))

    master.button_1.grid(row=2, column=0, pady=10, padx=20)

    # Add a second button
    master.button_2 = customtkinter.CTkButton(master=master.frame_left,
                                              text="Time Stretcher",
                                              fg_color=("gray75", "gray30"),
                                              command=lambda: f.change_to_frame2(master))

    master.button_2.grid(row=3, column=0, pady=10, padx=20)

    # Add a third button
    master.button_3 = customtkinter.CTkButton(master=master.frame_left,
                                              text="Pitch shifting",
                                              fg_color=("gray75", "gray30"),
                                              command=lambda: f.change_to_frame3(master))

    master.button_3.grid(row=4, column=0, pady=10, padx=20)

