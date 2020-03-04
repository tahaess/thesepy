# coding:utf-8

import numpy as np
from commpy.modulation import QAMModem
from komm import int2binlist
from commpy.utilities import hamming_dist

class qam(object):
    def __init__(self, mod_order, pack_size):
        self.mod_order = mod_order
        self.pack_size = pack_size


    def modulation_power(self):
        X = QAMModem(self.mod_order)
        x = np.reshape(np.fliplr(int2binlist(np.arange(0, self.mod_order, 1), int(np.sqrt(self.mod_order))).T), (1, self.mod_order * int(np.sqrt(self.mod_order))))
        xx = X.modulate(x[0])
        mod_power = np.sqrt(np.mean((xx) * (xx.T).conj().T))
        return mod_power

    def qammod(self):
        data = np.random.randint(2, size=self.pack_size)
        X = QAMModem(self.mod_order)
        Y = self.modulation_power()
        data_qam = X.modulate(data) / Y  # normalization
        return [data_qam, data]

    def qamdemod(self, received_data):
        X = QAMModem(self.mod_order)
        data_qamdemod = X.demodulate(received_data * self.modulation_power(),'hard',1)
        return data_qamdemod
