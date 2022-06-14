import sys
import os

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import numpy as np
import sounddevice as sd

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'models/'))
from Functions.models import utilFunctions as UF

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'transformations_interface/'))
from Functions.transformations_interface import sineTransformations_function as STrans

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'transformations/'))
from Functions.transformations import stftTransformations as stft


# Functions to play, browse and save
def play_song(y,fs):
    try:
        sd.play(y, fs)
    except Exception as e:
        print(e)

def stop_song(y):
    try:
        sd.stop(y)
    except Exception as e:
        print(e)

def browse_file1(master, case):

    filename = filedialog.askopenfilename(title="Please Select a File")
    try:
        if case ==1:

            master.y = None
            master.equalizer_frame.save_button.configure(state = DISABLED)
            filtering(master,1,filename)
            master.equalizer_frame.filelocation1.delete(0, END)
            master.equalizer_frame.filelocation1.insert(0, filename)

        elif case == 2:
            master.y2 = None
            master.stretcher_frame.save_button.configure(state=DISABLED)
            stretching(master,1,filename)
            master.stretcher_frame.filelocation_stretcher.delete(0, END)
            master.stretcher_frame.filelocation_stretcher.insert(0, filename)

        else:
            master.y3 = None
            master.pitch_frame.save_button.configure(state=DISABLED)
            shifting(master,1,filename)
            master.pitch_frame.filelocation_pitch.delete(0, END)
            master.pitch_frame.filelocation_pitch.insert(0, filename)

    except Exception as e:
        messagebox.showerror(message="File not supported", title="Something went wrong")
        print(e) #For developers

    return filename

def save_audio(y, fs):

    try:
        outputFile = filedialog.asksaveasfile(defaultextension=".wav")
        UF.wavwrite(y, fs, outputFile.name)
        messagebox.showinfo(message="Your file has been saved ", title="Well done!")


    except Exception:
        messagebox.showinfo(message="You have not saved the file ", title="Are you okay?")


#Functions to change between frames

def change_to_frame1(master):
    try:
        master.equalizer_frame.tkraise()

    except Exception:
        messagebox.showerror(message="Something went wrong", title="You can not get there!")

def change_to_frame2(master):
    try:
        master.stretcher_frame.tkraise()

    except Exception:
        messagebox.showerror(message="Something went wrong", title="You can not get there!")

def change_to_frame3(master):
    try:
        master.pitch_frame.tkraise()

    except Exception:
        messagebox.showerror(message="Something went wrong", title="You can not get there!")


#Functions to reset each slider individually

def reset_slider1(master):
    master.equalizer_frame.slider_1.set(0)

def reset_slider2(master):
    master.equalizer_frame.slider_2.set(0)

def reset_slider3(master):
    master.equalizer_frame.slider_3.set(0)

def reset_slider4(master):
    master.equalizer_frame.slider_4.set(0)

def reset_slider5(master):
    master.equalizer_frame.slider_5.set(0)

def reset_slider6(master):
    master.equalizer_frame.slider_6.set(0)

def reset_slider7(master):
    master.equalizer_frame.slider_7.set(0)

def reset_slider8(master):
    master.equalizer_frame.slider_8.set(0)

def reset_slider9(master):
    master.equalizer_frame.slider_9.set(0)

def reset_slider10(master):
    master.equalizer_frame.slider_10.set(0)

def reset_slider_pitch(master):
    master.pitch_frame.pitch_slider.set(0)

def reset_slider_stretcher(master):
    master.stretcher_frame.time_slider.set(1)

def forward_stretcher_slider(master):
    master.stretcher_frame.time_slider.set(master.stretcher_frame.time_slider.get()+1)

def backward_stretcher_slider(master):
    master.stretcher_frame.time_slider.set(master.stretcher_frame.time_slider.get()-1)

def forward_pitch_slider(master):
    master.pitch_frame.pitch_slider.set(master.pitch_frame.pitch_slider.get()+1)

def backward_pitch_slider(master):
    master.pitch_frame.pitch_slider.set(master.pitch_frame.pitch_slider.get()-1)


#Functions to equalize, time stretch and pitch shift

def filtering(master,case,filename):

    #Read the audio file
    (fs, x) = UF.wavread(filename)

    N = 2048

    sliders = [master.equalizer_frame.s1_current_value.get(), master.equalizer_frame.s2_current_value.get(),
               master.equalizer_frame.s3_current_value.get(), master.equalizer_frame.s4_current_value.get(),
               master.equalizer_frame.s5_current_value.get(), master.equalizer_frame.s6_current_value.get(),
               master.equalizer_frame.s7_current_value.get(), master.equalizer_frame.s8_current_value.get(),
               master.equalizer_frame.s9_current_value.get(), master.equalizer_frame.s10_current_value.get()]

    master.y, mX_plot, mY_plot, filt = stft.stftFiltering(x,fs,np.hanning(N),N,100,sliders)

    fig1 = Figure(figsize=(16, 9), dpi=100)
    fig1.set_facecolor('#2e2e2e')
    a = fig1.add_subplot(111)

    if (case == 2):
        a.plot(fs / 2 * np.arange(1, mX_plot.size + 1) / float(mX_plot.size), mY_plot, lw=1.5, label='mX')
        a.plot(fs / 2 * np.arange(1, mX_plot.size + 1) / float(mX_plot.size),filt + max(mX_plot), c ='0.5', lw=1.5, label='filter')
        a.legend(prop={'size': 10})
        a.axis([0, 20250, max(mX_plot)-60, max(mX_plot) + 10])
        a.spines['right'].set_visible(False)
        a.spines['top'].set_visible(False)
    else:
        a.plot(fs / 2 * np.arange(1, mX_plot.size + 1) / float(mX_plot.size), mX_plot, lw=1.5, label='mX')
        a.plot(fs / 2 * np.arange(1, mX_plot.size + 1) / float(mX_plot.size), filt + max(mX_plot), c ='0.5', lw=1.5, label='filter')
        a.legend(prop={'size': 10})
        a.axis([0, 20250, max(mX_plot)-60, max(mX_plot) + 10])
        a.spines['right'].set_visible(False)
        a.spines['top'].set_visible(False)

    canvas = FigureCanvasTkAgg(fig1, master.equalizer_frame)
    canvas.draw()
    canvas.get_tk_widget().configure(background='black', width=330, height=200)
    canvas.get_tk_widget().grid(row=6, column=0, sticky="w", padx=(220, 600), pady=(0,0))

    if case == 2: #If we pressed the button Equalize, we can save the file (case = 2)
        master.equalizer_frame.save_button.configure(state=NORMAL)

def stretching(master,case,filename):


    # Read the audio file
    (fs2, x2) = UF.wavread(filename)

    if case == 1:
        fig4 = Figure(figsize=(16, 9), dpi=100)
        fig4.set_facecolor('#2e2e2e')
        a4 = fig4.add_subplot(111)
        master.y2 = x2
        master.stretcher_frame.axis_size = master.y2.size
        a4.plot(np.arange(master.stretcher_frame.axis_size),master.y2)
        a4.axis('off')


        canvas4 = FigureCanvasTkAgg(fig4, master.stretcher_frame)
        canvas4.draw()
        canvas4.get_tk_widget().configure(background='black', width=720, height=200)
        canvas4.get_tk_widget().grid(row=2, column=0, sticky="w", padx=(20, 580), pady=(0, 0))

    else:
        fig4 = Figure(figsize=(16, 9), dpi=100)
        fig4.set_facecolor('#2e2e2e')
        a4 = fig4.add_subplot(111)

        inputFile2, fs2, tfreq2, tmag2 = STrans.analysis(master.stretcher_frame.filelocation_stretcher.get())

        master.y2 = STrans.transformation_synthesis(inputFile2, fs2, tfreq2, tmag2,freqScaling=np.array([0, 1, 1, 1]),timeScaling=np.array([0,0.0,1,master.stretcher_frame.speed_value.get()]))

        a4.plot(master.y2)
        a4.axis(xmin=0,xmax=master.stretcher_frame.axis_size)
        a4.axis('off')


        canvas4 = FigureCanvasTkAgg(fig4, master.stretcher_frame)
        canvas4.draw()
        canvas4.get_tk_widget().configure(background='black', width=720, height=200)
        canvas4.get_tk_widget().grid(row=2, column=0, sticky="w", padx=(20, 580), pady=(0, 0))

        master.stretcher_frame.save_button.configure(state=NORMAL)

def shifting(master,case,filename):

    # Read the audio file
    (fs3, x3) = UF.wavread(filename)

    if case == 1:

        fig6 = Figure(figsize=(16, 9), dpi=100)
        fig6.set_facecolor('#2e2e2e')
        a6 = fig6.add_subplot(111)

        master.y3 = x3

        a6.plot(master.y3)
        a6.axis('off')
        
        canvas6 = FigureCanvasTkAgg(fig6, master.pitch_frame)
        canvas6.draw()
        canvas6.get_tk_widget().configure(background='black', width=720, height=200)
        canvas6.get_tk_widget().grid(row=2, column=0, sticky="w", padx=(20, 580), pady=(0, 0))

    else:

        fig6 = Figure(figsize=(16, 9), dpi=100)
        fig6.set_facecolor('#2e2e2e')
        a6 = fig6.add_subplot(111)

        inputFile,fs,tfreq,tmag = STrans.analysis(filename)

        slider_value = master.pitch_frame.current_value.get()
        r = 2**(1/12) # semi-tons jumps

        master.y3 = STrans.transformation_synthesis(inputFile,fs,tfreq,tmag,freqScaling=np.array([0, r**slider_value, 1, r**slider_value]), timeScaling=np.array([0,0.0,1,1.0]))

        a6.plot(master.y3)
        a6.axis('off')

        canvas6 = FigureCanvasTkAgg(fig6, master.pitch_frame)
        canvas6.draw()
        canvas6.get_tk_widget().configure(background='black', width=720, height=200)
        canvas6.get_tk_widget().grid(row=2, column=0, sticky="w", padx=(20, 580), pady=(0,0))

        master.pitch_frame.save_button.configure(state=NORMAL)





