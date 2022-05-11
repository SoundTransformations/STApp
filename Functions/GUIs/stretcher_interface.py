import os
import sys
import customtkinter
import utilities as f

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../models/'))
from Functions.models import utilFunctions as UF


def stretcher_interface(master):

    ## CONFIGURE THE FRAME FOR THE STRETCHER

    # configure grid layout (3x7)
    master.stretcher_frame.rowconfigure((0, 1, 2, 3), weight=1)
    master.stretcher_frame.rowconfigure(7, weight=10)
    master.stretcher_frame.columnconfigure((0, 1), weight=1)
    master.stretcher_frame.columnconfigure(2, weight=0)

    ## INPUT FILE 1

    master.label_1 = customtkinter.CTkLabel(master=master.stretcher_frame,
                                            text="File1:",
                                            text_font=("Roboto Medium", -16),
                                            fg_color=("white", "gray30"),
                                            width=30)  # font name and size in px

    master.label_1.grid(row=0, column=0, pady=5, padx=50, sticky="w")

    master.stretcher_frame.filelocation1 = customtkinter.CTkEntry(master=master.stretcher_frame,
                                                                  width=10,
                                                                  placeholder_text="Path to the first input file")  # TEXTBOX TO PRINT PATH OF THE SOUND FILE

    master.stretcher_frame.filelocation1.grid(row=0, column=0, columnspan=2, pady=5, padx=(120, 200), sticky="we")
    master.stretcher_frame.filelocation1.focus_set()

    # Button to browse the input file 1
    open_file1 = customtkinter.CTkButton(master.stretcher_frame,
                                         text="...",
                                         width=3,
                                         command=lambda: f.browse_file1(master))

    open_file1.grid(row=0, column=0, columnspan=2, sticky="e", padx=(150, 160), pady=5)

    preview1 = customtkinter.CTkButton(master.stretcher_frame, text="Play!",
                                       width=3,
                                       command=lambda: UF.wavplay(master.stretcher_frame.filelocation1.get()),
                                       fg_color=("gray75", "gray30"),
                                       hover_color="green")

    preview1.grid(row=0, column=0, columnspan=3, sticky="e", padx=(250, 100), pady=5)