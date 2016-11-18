import numpy as np
import pylab as pl
import scipy.signal.signaltools as sigtool
import scipy.ndimage.filters as filters
import scipy.signal as signal
from scipy.signal import hilbert
from numpy.random import sample
from scipy import *
import matplotlib.pyplot as plt

#the following variables setup the system
Fc = 1000       #simulate a carrier frequency of 1kHz
Fbit = 50       #simulated bitrate of data
Fdev = 500      #frequency deviation, make higher than bitrate
N = 40        #how many bits to send
A = 1           #transmitted signal amplitude
Fs = 10000     #sampling frequency for the simulator, must be higher than twice the carrier frequency
A_n = 0.01      #noise peak amplitude
N_prntbits = 10 #number of bits to print in plots

def plot_data(y):
    #view the data in time and frequency domain
    #calculate the frequency domain for viewing purposes
    N_FFT = float(len(y))
    f = np.arange(0,Fs/2,Fs/N_FFT)
    w = np.hanning(len(y))
    y_f = np.fft.fft(np.multiply(y,w))
    y_f = 10*np.log10(np.abs(y_f[0:N_FFT/2]/N_FFT))
    pl.xlabel('Time (s)')
    pl.ylabel('Frequency (Hz)')
    pl.title('Original VCO output versus time')
    pl.grid(True)
    pl.subplot(2,1,1)
    pl.plot(t[0:Fs*N_prntbits/Fbit],y[0:Fs*N_prntbits/Fbit])
    pl.xlabel('Time (s)')
    pl.ylabel('Amplitude (V)')
    pl.title('Amplitude of carrier versus time')
    pl.grid(True)
    pl.subplot(2,1,2)
    pl.plot(f[0:(Fc+Fdev*2)*N_FFT/Fs],y_f[0:(Fc+Fdev*2)*N_FFT/Fs])
    pl.xlabel('Frequency (Hz)')
    pl.ylabel('Amplitude (dB)')
    pl.title('Spectrum')
    pl.grid(True)
    pl.tight_layout()
    pl.show()
  


t = np.arange(0,float(N)/float(Fbit),1/float(Fs), dtype=np.float)  
"""
Data in
"""
#generate some random data for testing
data_in = np.random.random_integers(0,1,N)
print "data input" ,data_in
#data_in=np.ones(N)

def data_in_modf(data_in):
    data_in_modified=np.array([])
    for bit in data_in:
        temp_data=np.ones(Fs/Fbit)
        if bit ==0:
            temp_data=-1*temp_data

        data_in_modified=np.hstack((data_in_modified,temp_data))

    return data_in_modified
"""
VCO
"""

data_in_modified=data_in_modf(data_in)

filters.gaussian_filter(data_in_modified, 20, order=0, output=data_in_modified)

plt.plot(t,data_in_modified)
plt.show()

#print "data in",data_in,data_in_modified



c_t=[0 for i in range(len(data_in_modified))]

for i in range(len(data_in_modified)):
    c_t[i]=c_t[i-1]+data_in_modified[i]




c_t=np.array(c_t)
c_t=10*c_t/Fs
#scipy.ndimage.filters.gaussian_filter(c_t, sigma)

cos_ct=np.cos(c_t)
sin_ct=np.sin(c_t)

carrier_cos=np.cos(2*np.pi*Fc*t)
carrier_sin=np.sin(2*np.pi*Fc*t)

in_comp=np.multiply(cos_ct,carrier_cos)
quad_comp=np.multiply(sin_ct,carrier_sin)

# plt.plot(t,sin_ct)#,t,quad_comp)
# plt.show()

yt=in_comp-quad_comp

plot_data(yt)

####################### Multiplying by complex number###################

analytical_yt=hilbert(yt)

analytical_yt=analytical_yt*(1+1j)

yt_modified=analytical_yt.real

plot_data(yt_modified)


###########################noise section############################

# noise = (np.random.randn(len(yt)))*A_n
# snr = 10*np.log10(np.mean(np.square(yt)) / np.mean(np.square(noise)))
# print "SNR = %fdB" % snr
# yt=np.add(yt,noise)
# #view the data after adding noise
# plot_data(yt)


#####################demodulate###########################

h=signal.firwin( numtaps=50, cutoff=300, nyq=Fs)


cos_phi_mul=np.multiply(yt,carrier_cos)
sin_phi_mul=np.multiply(yt,carrier_sin)
cos_phi_filt=signal.lfilter( h, 1.0, cos_phi_mul)
sin_phi_filt=signal.lfilter( h, 1.0, sin_phi_mul)


tan_inv=np.arctan(sin_phi_filt/cos_phi_filt)
sin_inv=np.arcsin(sin_phi_filt)


# plt.plot(t,sin_phi_filt,'g')
plt.plot(t,100*data_in_modified,'k',linewidth='2')
# plt.plot(t,cos_phi_filt)


out=np.diff(sin_inv)*Fs
out=np.hstack((0,out))

# out=out[25:len(yt)]

# out=np.hstack((out,np.zeros(25)))
plt.plot(t,-1*out,'r')
# out_env = np.abs(sigtool.hilbert(out))
# plt.plot(t,out_env,'m')


######calculating BER################

BitError=0
for i in range(len(data_in)):
	total=0
	for j in range(0,int(0.5*Fs/Fbit)):

		if abs(out[i*Fs/Fbit+2*j])<100:
			total+=out[i*Fs/Fbit+2*j]

	if total>=0:
		bit=0
	else:
		bit=1

	print bit ,

	if data_in[i]!=bit:
		BitError+=1

print 
print "Total Error Bits",BitError*100.0/len(data_in),"%"
plt.show()






