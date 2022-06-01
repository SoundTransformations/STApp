import sys
import os
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import numpy as np
import sounddevice as sd

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'models/'))
from Functions.models import utilFunctions as UF
from Functions.models import dftModel as DFT

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'transformations_interface/'))
from Functions.transformations_interface import stftMorph_function as sT
from Functions.transformations_interface import sineTransformations_function as STrans

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'transformations/'))
from Functions.transformations import stftTransformations as stft


# Functions
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

    if case ==1:
        try:
            master.equalizer_frame.filelocation1.delete(0, END)
            master.equalizer_frame.filelocation1.insert(0, filename)
            master.y = None
            master.equalizer_frame.save_button.configure(state = DISABLED)
            filtering(master,1)

        except Exception:
            messagebox.showerror(message = "We can not open that file", title = "Error opening the file")

    elif case ==2:
        try:

            master.stretcher_frame.filelocation_stretcher.delete(0, END)
            master.stretcher_frame.filelocation_stretcher.insert(0, filename)
            master.y2 = None
            stretching(master)

        except Exception:
            messagebox.showerror(message = "We can not open that file", title = "Error opening the file")

    else:
        try:
            master.pitch_frame.filelocation_pitch.delete(0, END)
            master.pitch_frame.filelocation_pitch.insert(0, filename)
            master.y3 = None
            shifting(master,1)

        except Exception as e:
            messagebox.showerror(message=str(e), title="Error opening the file")

    return filename

def transformation_synthesis(master):
    try:
        inputFile1 = master.filelocation1.get()
        inputFile2 = master.filelocation2.get()
        window1 = master.w1_type.get()
        window2 = master.w2_type.get()
        M1 = int(master.M1.get())
        M2 = int(master.M2.get())
        N1 = int(master.N1.get())
        N2 = int(master.N2.get())
        H1 = int(master.H1.get())
        smoothf = float(master.smoothf.get())
        balancef = float(master.balancef.get())
        y, fs = sT.main(inputFile1, inputFile2, window1, window2, M1, M2, N1, N2, H1, smoothf, balancef)
        save_audio(y, fs)

    except ValueError:
        messagebox.showerror("Input values error")

def save_audio(y, fs):

    try:
        outputFile = filedialog.asksaveasfile(defaultextension=".wav")
        UF.wavwrite(y, fs, outputFile.name)

    except Exception:
        messagebox.showerror(message="We can not save this file", title="Something went wrong!")

def button_event():
    print("Button pressed")

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


def filtering(master,case):

    try:
        #Read the audio file
        (fs,x) = UF.wavread(master.equalizer_frame.filelocation1.get())

        #We analyze one fragment of the the sound
        N = 2048
        start = int(1.0 * fs)
        x1 = x[start:start + N]
        mX, pX = DFT.dftAnal(x1, np.hamming(N), N)

        #Build the filt array
        startBin = 0 #int(N * 1 / fs)
        nBins = 183 #int(N * 1000 / fs)
        db_to_down = 60

        sliders = [master.equalizer_frame.s1_current_value.get(),
                   master.equalizer_frame.s2_current_value.get(),
                   master.equalizer_frame.s3_current_value.get(),
                   master.equalizer_frame.s4_current_value.get(),
                   master.equalizer_frame.s5_current_value.get(),
                   master.equalizer_frame.s6_current_value.get(),
                   master.equalizer_frame.s7_current_value.get(),
                   master.equalizer_frame.s8_current_value.get(),
                   master.equalizer_frame.s9_current_value.get(),
                   master.equalizer_frame.s10_current_value.get()]

        filt = np.zeros(mX.size) - 60
        bandpass1 = (np.hanning(nBins) * (db_to_down+int(sliders[0]))) - db_to_down
        filt[startBin : startBin + int((nBins)/2)+1] = bandpass1[int((nBins)/2):]

        for i in range(1,10):
            bandpass = (np.hanning(nBins) * (db_to_down+int(sliders[i])))
            filt[startBin+i*91-int(nBins/2):startBin +i*91-int(nBins/2) +nBins] += bandpass

        master.y = stft.stftFiltering(x,fs,np.hanning(N),N,100,filt)

        fig1 = Figure(figsize=(16, 9), dpi=100)
        fig1.set_facecolor('#2e2e2e')
        a = fig1.add_subplot(111)
        try:
            a.plot(np.arange(N) / float(fs), x1 * np.hamming(N), 'b', lw=1.5)
            a.plot(mX, lw=1.5, label='mX')
            a.plot(filt + max(mX), 'k', lw=1.5, label='filter')
            a.legend(prop={'size': 10})
            a.axis([0, mX.size, -90, max(mX) + 10])
            a.spines['right'].set_visible(False)
            a.spines['top'].set_visible(False)

        except Exception:
            a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 5])

        canvas = FigureCanvasTkAgg(fig1, master.equalizer_frame)
        canvas.draw()
        canvas.get_tk_widget().configure(background='black', width=300, height=200)
        canvas.get_tk_widget().grid(row=6, column=0, sticky="w", padx=(250, 600), pady=(0,0))

        if case == 2: #If we pressed the button Equalize, we can save the file (case = 2)
            master.equalizer_frame.save_button.configure(state=NORMAL)

    except Exception:
        messagebox.showinfo(message="You have not loaded any file", title= "File not loaded!")

def stretching(master):

    try:
        #Read the audio file
        (fs2,x2) = UF.wavread(master.stretcher_frame.filelocation_stretcher.get())

        fig4 = Figure(figsize=(16, 9), dpi=100)
        fig4.set_facecolor('#2e2e2e')
        a4 = fig4.add_subplot(111)
        master.y2 = x2
        try:
            a4.plot(master.y2)
            #a2.legend(prop={'size': 10})
            #a2.axis([0, x2.size, -90, max(x2) + 10])
            a4.axis('off')
        except Exception:
            a4.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 5])

        canvas4 = FigureCanvasTkAgg(fig4, master.stretcher_frame)
        canvas4.draw()
        canvas4.get_tk_widget().configure(background='black', width=720, height=200)
        canvas4.get_tk_widget().grid(row=2, column=0, sticky="w", padx=(20, 580), pady=(0,0))


    except Exception:
        messagebox.showinfo(message="You have not loaded any file", title= "File not loaded!")

def shifting(master,case):

    # Read the audio file
    (fs3, x3) = UF.wavread(master.pitch_frame.filelocation_pitch.get())

    if case == 1:
        try:

            fig6 = Figure(figsize=(16, 9), dpi=100)
            fig6.set_facecolor('#2e2e2e')
            a6 = fig6.add_subplot(111)

            master.y3 = x3

            try:
                a6.plot(master.y3)
                a6.axis('off')
            except Exception:
                a6.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 5])

            canvas6 = FigureCanvasTkAgg(fig6, master.pitch_frame)
            canvas6.draw()
            canvas6.get_tk_widget().configure(background='black', width=720, height=200)
            canvas6.get_tk_widget().grid(row=2, column=0, sticky="w", padx=(20, 580), pady=(0, 0))

        except Exception:
           messagebox.showinfo(message="You have not loaded any file", title= "File not loaded!")

    else:
        try:

            fig6 = Figure(figsize=(16, 9), dpi=100)
            fig6.set_facecolor('#2e2e2e')
            a6 = fig6.add_subplot(111)

            inputFile,fs,tfreq,tmag = STrans.analysis(master.pitch_frame.filelocation_pitch.get())

            master.y3 = STrans.transformation_synthesis(inputFile,fs,tfreq,tmag,freqScaling=np.array([0, 0.6, 1, 0.6]), timeScaling=np.array([0,0.0,1,1.0]))

            try:
                a6.plot(master.y3)
                a6.axis('off')
            except Exception:
                a6.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 5])

            canvas6 = FigureCanvasTkAgg(fig6, master.pitch_frame)
            canvas6.draw()
            canvas6.get_tk_widget().configure(background='black', width=720, height=200)
            canvas6.get_tk_widget().grid(row=2, column=0, sticky="w", padx=(20, 580), pady=(0,0))

        except Exception as e:
            messagebox.showinfo(message=str(e), title= "File not loaded!")




