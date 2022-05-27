import sys
import os
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
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'transformations/'))
from Functions.transformations import stftTransformations as stft


# Functions
def play_song(y,fs):
    try:
        sd.play(y, fs)

    except Exception as e:
        print(e)

def browse_file1(master, case):

    filename = filedialog.askopenfilename(title="Please Select a File")

    if case ==1:
        try:
            master.equalizer_frame.filelocation1.delete(0, END)
            master.equalizer_frame.filelocation1.insert(0, filename)
            master.y = None
            filtering(master)

        except Exception:
            messagebox.showerror(message = "We can not open that file", title = "Error opening the file")

    elif case ==2:
        try:

            master.stretcher_frame.filelocation1.delete(0, END)
            master.stretcher_frame.filelocation1.insert(0, filename)
            master.y2 = None
            stretching(master)

        except Exception:
            messagebox.showerror(message = "We can not open that file", title = "Error opening the file")

    else:
        try:
            master.other_interface.filelocation1.delete(0, END)
            master.other_interface.filelocation1.insert(0, filename)
            master.y3 = None
            shifting(master)

        except Exception:
            messagebox.showerror(message="We can not open that file", title="Error opening the file")

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
        outputFile = filedialog.asksaveasfile()
        UF.wavwrite(y, fs, outputFile.name + '_stftMorph.wav')

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
        master.other_interface.tkraise()

    except Exception:
        messagebox.showerror(message="Something went wrong", title="You can not get there!")

def reset_slider1(master):
    master.slider_5.set(0)

def reset_slider2(master):
    master.slider_6.set(0)

def reset_slider3(master):
    master.slider_7.set(0)

def reset_slider4(master):
    master.slider_8.set(0)

def reset_slider5(master):
    master.slider_1.set(0)

def reset_slider6(master):
    master.slider_9.set(0)

def reset_slider7(master):
    master.slider_10.set(0)

def reset_slider8(master):
    master.slider_11.set(0)

def reset_slider9(master):
    master.slider_12.set(0)

def reset_slider10(master):
    master.slider_13.set(0)


def filtering(master):

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

        sliders = [master.current_value1.get(),
                   master.current_value2.get(),
                   master.current_value3.get(),
                   master.current_value4.get(),
                   master.current_value5.get(),
                   master.current_value6.get(),
                   master.current_value7.get(),
                   master.current_value8.get(),
                   master.current_value9.get(),
                   master.current_value10.get()]

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

        except Exception:
            a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 5])

        canvas = FigureCanvasTkAgg(fig1, master.equalizer_frame)
        canvas.draw()
        canvas.get_tk_widget().configure(background='black', width=300, height=200)
        canvas.get_tk_widget().grid(row=6, column=0, sticky="w", padx=(250, 600), pady=(0,0))


    except Exception:
        messagebox.showinfo(message="You have not loaded any file", title= "File not loaded!")

def stretching(master):

    try:
        #Read the audio file
        (fs2,x2) = UF.wavread(master.stretcher_frame.filelocation1.get())


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

def shifting(master):

    try:
        #Read the audio file
        (fs3,x3) = UF.wavread(master.other_interface.filelocation1.get())

        fig6 = Figure(figsize=(16, 9), dpi=100)
        fig6.set_facecolor('#2e2e2e')
        a6 = fig6.add_subplot(111)
        master.y3 = x3
        try:
            a6.plot(master.y3)
            a6.axis('off')
        except Exception:
            a6.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 5])

        canvas6 = FigureCanvasTkAgg(fig6, master.other_interface)
        canvas6.draw()
        canvas6.get_tk_widget().configure(background='black', width=720, height=200)
        canvas6.get_tk_widget().grid(row=2, column=0, sticky="w", padx=(20, 580), pady=(0,0))

    except Exception:
        messagebox.showinfo(message="You have not loaded any file", title= "File not loaded!")


def sineFreqScaling(master):
    """
    Frequency scaling of sinusoidal tracks
    sfreq: frequencies of input sinusoidal tracks
    freqScaling: scaling factors, in time-value pairs (value of 1 is no scaling)
    returns ysfreq: frequencies of output sinusoidal tracks
    """
    (fs,x) = UF.wavread(master.other_interface.filelocation1.get())
    N = 2048
    mX, pX = DFT.dftAnal(x, np.hamming(N), N)
    sfreq = mX
    freqScaling = (master.current_value.get())

    if (freqScaling.size % 2 != 0):                        # raise exception if array not even length
        raise ValueError("Frequency scaling array does not have an even size")

    L = sfreq.shape[0]                                     # number of input frames
    # create interpolation object from the scaling values
    freqScalingEnv = np.interp(np.arange(L), L*freqScaling[::2]/freqScaling[-2], freqScaling[1::2])
    ysfreq = np.zeros_like(sfreq)                          # create empty output matrix
    for l in range(L):                                     # go through all frames
        ind_valid = np.where(sfreq[l,:]!=0)[0]               # check if there are frequency values
        if ind_valid.size == 0:                              # if no values go to next frame
            continue
        ysfreq[l,ind_valid] = sfreq[l,ind_valid] * freqScalingEnv[l] # scale of frequencies

    sd.play(ysfreq, fs)


