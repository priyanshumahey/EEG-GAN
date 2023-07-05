from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

class process():
    def __init__():
        """
        This class is used to preprocess the data.
        The input is a dict with a key 'V' containing the voltage data.
        """
        return

    def preprocess(data):
        V = data['V'].astype('float32')
        b, a = signal.butter(3, [50], btype='high', fs=1000)
        V = signal.filtfilt(b, a, V, 0)
        V = np.abs(V)**2
        b, a = signal.butter(3, [10], btype='low', fs=1000)
        V = signal.filtfilt(b, a, V, 0)
        V = V/V.mean(0)
        return V

class plots():
    def __init__():
        """
        For plotting the dataset
        """
        return

    def singlechannel1(data, channel, trange, title=''):
        plt.figure(figsize=(20,10))
        if title:
            plt.suptitle(title, fontsize=20)
        plt.plot(trange, data[:,channel])
        plt.title('ch%d'%channel)
        plt.xticks([0, 1000, 2000])
        plt.ylim([0, 4])

    def singlechannel2(data, data2, channel, trange, title=''):
        plt.figure(figsize=(20,10))
        if title:
            plt.suptitle(title, fontsize=20)
        plt.plot(trange, data[:,channel])
        plt.plot(trange, data2[:,channel])
        plt.title('ch%d'%channel)
        plt.xticks([0, 1000, 2000])
        plt.ylim([0, 4])

    def all_channels1(data, trange, title=''):
        plt.figure(figsize=(20,10))
        if title:
            plt.suptitle(title, fontsize=20)
        for j in range(46):
            ax = plt.subplot(5,10,j+1)
            plt.plot(trange, data[:,j])
            plt.title('ch%d'%j)
            plt.xticks([0, 1000, 2000])
            plt.ylim([0, 4])

    def all_channels2(data, data2, trange, title=''):
        plt.figure(figsize=(20,10))
        if title:
            plt.suptitle(title, fontsize=20)
        for j in range(46):
            ax = plt.subplot(5,10,j+1)
            plt.plot(trange, data[:,j])
            plt.plot(trange, data2[:,j])
            plt.title('ch%d'%j)
            plt.xticks([0, 1000, 2000])
            plt.ylim([0, 4])