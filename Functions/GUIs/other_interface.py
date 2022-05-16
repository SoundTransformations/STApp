import os
import sys
import customtkinter
from Functions import utilities as f

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../models/'))
from Functions.models import utilFunctions as UF


def create_other_interface(master):
    ## CONFIGURE THE EQUALIZER FRAME

    # Configure grid layout (3x7)
    master.other_interface.rowconfigure(1, weight=0)

    master.label = customtkinter.CTkLabel(master=master.other_interface,
                                          text="test_interface",
                                          text_font=("Roboto Medium", -30),
                                          fg_color=("white", "gray18"),
                                          width=30)  # font name and size in px

    master.label.grid(row=0, column=0, pady=(15, 0), padx=40, sticky="w")