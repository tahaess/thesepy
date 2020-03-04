#coding:utf-8

import numpy as np
from scipy.fftpack import fft, ifft



class optical_fft(object):
    nOfdmSymbol: int

    def __init__(self, data, Nfft, cp):
        self.data = data
        self.nfft = Nfft
        self.cp = cp
        self.fftSize = (self.nfft + 1) * 2
        self.nOfdmSymbol = int(len(self.data) / self.nfft)
        self.blkSize = self.fftSize + self.cp

    def dco_modulator(self):
        if len(self.data) % self.nfft != 0:
            raise Exception("lenght of data should be divided on subcarrier number")
        if self.nfft >= len(self.data):
            raise Exception("Number of subcarrier is too low")
        for j in range (0,self.nOfdmSymbol):
            #data_vector = np.zeros((self.nfft,self.nOfdmSymbol),dtype=complex)
            #data_vector[j] = self.data[:(j+1)*self.nOfdmSymbol]
            self.outt = np.zeros((len(self.data),1),dtype=complex)
            self.outt[(j*self.nfft)+1:(j+1)*self.nfft] = ifft(np.concatenate(0,self.data[(j*self.nOfdmSymbol)+1) : (j+1)*self.nOfdmSymbol],0,np.fliplr(np.conj(self.data[(j*self.nOfdmSymbol)+1):(j+1)*self.nOfdmSymbol]).T).T),self.nfft,axis=0)
        return outt
        #data_matrix = np.reshape(self.data, (self.nfft, self.nOfdmSymbol))
        #self.out = np.zeros((self.blkSize, self.nOfdmSymbol),dtype=complex)
        #self.out[self.cp:, :] = np.sqrt(self.fftSize) * ifft(np.concatenate((np.zeros((1, self.nOfdmSymbol)), data_matrix, np.zeros((1, self.nOfdmSymbol)), np.fliplr(np.conj(data_matrix).T).T), axis=0))
        #self.out[:self.cp, :] = self.out[-self.cp:]
        #out = np.reshape(self.out, (self.blkSize * self.nOfdmSymbol, 1))
        #return out

    def dco_demodulation(self,received_signal):#,total_coeff_channel):
        # manage exceptions later for number of subcarrier should be divided by 2**2
        if len(self.data) % self.nfft != 0:
            raise Exception("wrong input size for demodulation")
        self.out = np.zeros((self.nfft*self.nOfdmSymbol,1),dtype=complex)

        for i in range(0,self.nOfdmSymbol):
            in_received_signal = received_signal[i*self.blkSize:i+1*self.blkSize]
            # cp removal
            in_cp_removal = in_received_signal[self.cp:]
            #normilized fft
            in_fft = 1/np.sqrt(self.fftSize)*fft(in_cp_removal,self.fftSize,axis=0)
            # one tape zero forcing equalizer
            #channel_FR = fft(total_coeff_channel,self.fftSize)
            #estimate_channel_FR = channel_FR[1:self.fftSize]
            #in_fft[1:self.nfft] = in_fft[1:self.nfft]/estimate_channel_FR
            # hermitian symetry removal
            in_hs_removal = in_fft[1:self.nfft+1]
            self.out[i*self.nfft:(i+1)*self.nfft] = in_hs_removal
        return self.out









