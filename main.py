from optical_ofdm import optical_ofdm
from qam.qam import qam
import numpy as np
from optical_ofdm.optical_ofdm import optical_fft
from commpy.modulation import QAMModem
import matplotlib.pyplot as plt
import seaborn as sns

m=16
n=1024
nfft = 64
cp = 10

modulation_qam = qam(m,n)
[df,dd] = modulation_qam.qammod()
dco_ofdm = optical_fft(df,nfft,cp)
fg = dco_ofdm.dco_modulator()
gf = dco_ofdm.dco_demodulation(fg)
ds = modulation_qam.qamdemod(gf)


from commpy.utilities import hamming_dist
a = hamming_dist(ds,dd)
print("ds",a)

#x = optical_ofdm.optical_fft(data_qam, 64, 10)
#s = x.dco_modulator()

#print("vector after ifft",s)
#plt.plot(s)
#sns.scatterplot(np.real(data_qam),np.imag(data_qam))
#plt.show()

