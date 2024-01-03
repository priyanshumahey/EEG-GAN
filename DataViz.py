from pathlib import Path
import os
import mne
import numpy as np 
import tkinter as tk
from tkinter import filedialog
import mne
import matplotlib.pyplot as plt

t_min, t_max = -1., 4.
event_id = {'hands': 2, 'feet': 3}

import matplotlib.pyplot as plt

def choose_file():
    file_path = filedialog.askopenfilename(initialdir="./MNE-eegbci-data/files/eegmmidb/1.0.0", title="Select Data File")
    if file_path:
        global raw
        raw = mne.io.read_raw_edf(file_path, preload=True, verbose=False)
        mne.datasets.eegbci.standardize(raw)
        montage = mne.channels.make_standard_montage("standard_1005")
        raw.set_montage(montage)
        global raw_3ch
        raw_3ch = raw.copy()
        raw_3ch = raw_3ch.pick_channels(['C3', 'Cz', 'C4'])

def plot_raw():
    raw.plot()

def plot_sensors():
    raw.plot_sensors(show_names=True)

def plot_channels():
    raw.plot(n_channels=1)

def plot_3ch():
    raw_3ch.plot()

def plot_events():
    event_dict = {'T0': 1, 'T1': 2, 'T2': 3}
    events = mne.events_from_annotations(raw_3ch)
    fig = mne.viz.plot_events(events[0], event_id=event_dict, sfreq=raw_3ch.info['sfreq'])
    plt.show()

def plot_psd():
    raw.plot_psd()

def plot_psd_3ch():
    raw_3ch.plot_psd()

def topomap():
    raw.plot_psd_topomap(ch_type='eeg', normalize=True)

root = tk.Tk()

choose_file_button = tk.Button(root, text="Choose Data File", command=choose_file)
choose_file_button.pack()

plot_raw_button = tk.Button(root, text="Plot Raw Data", command=plot_raw)
plot_raw_button.pack()

plot_sensors_button = tk.Button(root, text="Plot Sensors", command=plot_sensors)
plot_sensors_button.pack()

plot_channels_button = tk.Button(root, text="Plot Channels", command=plot_channels)
plot_channels_button.pack()

plot_3ch_button = tk.Button(root, text="Plot 3 Channels", command=plot_3ch)
plot_3ch_button.pack()

plot_events_button = tk.Button(root, text="Plot Events", command=plot_events)
plot_events_button.pack()

plot_psd_button = tk.Button(root, text="Plot PSD", command=plot_psd)
plot_psd_button.pack()

plot_psd_3ch_button = tk.Button(root, text="Plot PSD 3 Channels", command=plot_psd_3ch)
plot_psd_3ch_button.pack()

topomap_button = tk.Button(root, text="Plot Topomap", command=topomap)
topomap_button.pack()



root.mainloop()

