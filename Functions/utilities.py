import sys
import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import numpy as np
import sounddevice as sd

import matplotlib.pyplot as plt

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'models/'))
from Functions.models import utilFunctions as UF
from Functions.models import dftModel as DFT
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'transformations_interface/'))
from Functions.transformations_interface import stftMorph_function as sT
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'transformations/'))
from Functions.transformations import stftTransformations as stft


# Functions
def play_song():
    try:
        filename = filedialog.askopenfilename()
        UF.wavplay(filename)

    except Exception as e:
        print(e)

def browse_file1(master):
    try:
        filename = filedialog.askopenfilename(title="Please Select a File")
        master.equalizer_frame.filelocation1.delete(0, END)
        master.equalizer_frame.filelocation1.insert(0, filename)
        master.stretcher_frame.filelocation1.delete(0, END)
        master.stretcher_frame.filelocation1.insert(0, filename)
        return filename
    except Exception as e:
        messagebox.showerror("We can not open that file")

def browse_file2(master):
    try:
        filename = filedialog.askopenfilename(title="Please Select a File")
        master.filelocation2.delete(0, END)
        master.filelocation2.insert(0, filename)

    except Exception as e:
        print(e)

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
        messagebox.showerror("We can not save this file")

def button_event():
    print("Button pressed")

def change_to_frame1(master):
    try:
        master.equalizer_frame.tkraise()

    except Exception:
        messagebox.showerror("Something went wrong")

def change_to_frame2(master):
    try:
        master.stretcher_frame.tkraise()

    except Exception:
        messagebox.showerror("Something went wrong")

def change_to_frame3(master):
    try:
        master.other_interface.tkraise()

    except Exception:
        messagebox.showerror("Something went wrong")

def filtering(master):

    #Read the audio file
    (fs,x) = UF.wavread(master.equalizer_frame.filelocation1.get())

    #We analyze the sound
    N = 2048
    start = int(1.0 * fs)
    x1 = x[start:start + N]
    mX, pX = DFT.dftAnal(x1, np.hamming(N), N)


    #Iteratively fill an array of arrays called bandpass, which contains all the bandpasses at the different frequencies
    startBin = int(N * 1 / fs)
    nBins = int(N * 1000 / fs)
    bandpass = (np.hanning(nBins) *60) + int(master.current_value1.get()) -60
    bandpass2 = (np.hanning(nBins) *60) + int(master.current_value2.get()) -60
    bandpass3 = (np.hanning(nBins) *60) + int(master.current_value3.get())-60
    filt = np.zeros(mX.size) - 60
    filt[startBin:startBin + nBins] = bandpass
    filt[startBin+nBins:startBin+nBins+nBins] = bandpass2
    #filt[startBin+20:startBin+20+nBins] = filt[startBin+20:startBin+20+nBins]-bandpass2 #filt[startBin+20:startBin+20+nBins]
    #filt[startBin+nBins+nBins:startBin+nBins+nBins+nBins] = bandpass3 #filt[startBin+20:startBin+20+nBins]


    y = stft.stftFiltering(x,fs,np.hanning(N),N,100,filt)

    plt.figure(1, figsize=(10, 4))
    plt.subplot(121)
    plt.plot(np.arange(N) / float(fs), x1 * np.hamming(N), 'b', lw=1.5)
    plt.axis([0, N / float(fs), min(x1 * np.hamming(N)), max(x1 * np.hamming(N))])
    plt.title('input sound')

    plt.subplot(122)
    plt.plot(fs * np.arange(mX.size) / float(mX.size), mX, 'r', lw=1.5, label='mX')
    plt.plot(fs * np.arange(mX.size) / float(mX.size), filt + max(mX), 'k', lw=1.5, label='filter')
    plt.legend(prop={'size': 10})
    plt.axis([0, fs / 4.0, -90, max(mX) + 2])
    plt.title('mX + filter')


    plt.show()

    sd.play(y, fs)