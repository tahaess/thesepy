from optical_ofdm import optical_ofdm
import numpy as np
from commpy.modulation import QAMModem
import matplotlib.pyplot as plt
import seaborn as sns

m=16;
n=1024;
data = np.random.randint(2, size=n)
qam = QAMModem(16)
data_qam = qam.modulate(data)
x = optical_ofdm.optical_fft(data_qam, 64, 10)
s = x.dco_modulator()

print("vector after ifft",s)
#plt.plot(s)
sns.scatterplot(np.real(data_qam),np.imag(data_qam))
plt.show()

