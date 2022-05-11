import customtkinter
from Functions import utilities as f


def create_main_interface(master):

    # Create the Menu Selector Frame
    master.frame_left = customtkinter.CTkFrame(master=master, width=180, corner_radius=0)
    master.frame_left.grid(row=0, column=0, sticky="nswe")

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

    # Add a Label
    master.label_1 = customtkinter.CTkLabel(master=master.frame_left,
                                            text="STApp",
                                            text_font=("Roboto Medium", -16))  # font name and size in px

    master.label_1.grid(row=1, column=0, pady=10, padx=10)

    # Add a button
    master.button_1 = customtkinter.CTkButton(master=master.frame_left,
                                              text="Equalizer",
                                              fg_color=("gray75", "gray30"),
                                              command=lambda: f.change_to_frame1(master))

    master.button_1.grid(row=2, column=0, pady=10, padx=20)

    # Add a second button
    master.button_2 = customtkinter.CTkButton(master=master.frame_left,
                                              text="Stretcher",
                                              fg_color=("gray75", "gray30"),
                                              command=lambda: f.change_to_frame2(master))

    master.button_2.grid(row=3, column=0, pady=10, padx=20)

    # Add a third button
    master.button_3 = customtkinter.CTkButton(master=master.frame_left,
                                              text="Relantizer",
                                              fg_color=("gray75", "gray30"),
                                              command=f.button_event)

    master.button_3.grid(row=4, column=0, pady=10, padx=20)

