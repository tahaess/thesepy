#coding:utf-8

import numpy as np
from scipy.fftpack import fft, ifft



class optical_fft(object):
    def __init__(self, data, Nfft, cp):
        self.data = data
        self.nfft = Nfft
        self.cp = cp

    def dco_modulator(self):
        if len(self.data) % self.nfft != 0:
            raise Exception("lenght of data should be divided on subcarrier number")
        if self.nfft >= len(self.data):
            raise Exception("Number of subcarrier is too low")
        fftSize = (self.nfft+ 1) * 2
        nOfdmSymbol = int(len(self.data) / self.nfft)
        blkSize = fftSize + self.cp
        datA = np.reshape(self.data, (self.nfft, nOfdmSymbol))
        self.out = np.zeros((blkSize, nOfdmSymbol))#,dtype=complex)
        self.out[self.cp:, :] = np.sqrt(fftSize) * ifft(np.concatenate((np.zeros((1, nOfdmSymbol)), datA, np.zeros((1, nOfdmSymbol)), np.fliplr(np.conj(datA).T).T), axis=0))
        self.out[:self.cp, :] = self.out[-self.cp:, :]
        out = np.reshape(self.out, (blkSize * nOfdmSymbol, 1))
        return out




