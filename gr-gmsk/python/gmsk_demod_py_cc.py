#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2016 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from gnuradio import gr
import scipy.ndimage.filters as filters
import scipy.signal as signal

class gmsk_demod_py_cc(gr.sync_block):
    """
    docstring for block gmsk_demod_py_cc
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name="gmsk_demod_py_cc",
            in_sig=[numpy.complex64],
            out_sig=[numpy.float32])


    def work(self, input_items, output_items):

        Fc = 1000       #simulate a carrier frequency of 1kHz
        Fbit = 50       #simulated bitrate of data
        Fdev = 5000      #frequency deviation, make higher than bitrate
        N = 100        #how many bits to send
        A = 1           #transmitted signal amplitude
        Fs = 10000     #sampling frequency for the simulator, must be higher than twice the carrier frequency
        A_n = 0.01      #noise peak amplitude
        N_prntbits = 10 #number of bits to print in plots
        in0 = input_items[0]
        out = output_items[0]
        # <+signal processing here+>

        h=signal.firwin( numtaps=50, cutoff=500, nyq=Fs)

        print "demodulator input:", len(in0)
        sin_phi_mul=in0.imag
        cos_phi_mul=in0.real
        
        cos_phi_filt=signal.lfilter( h, 1.0, cos_phi_mul)
        sin_phi_filt=signal.lfilter( h, 1.0, sin_phi_mul)

        sin_inv=numpy.arcsin(sin_phi_filt)
        tan_inv=numpy.arctan(sin_phi_filt/cos_phi_filt)

        demodulated=numpy.diff(sin_inv)*Fs
        demodulated=numpy.hstack((0,demodulated))

        # demodulated=demodulated[25:len(in0)]

        # demodulated=numpy.hstack((demodulated,numpy.zeros(25)))
        
        out[:] = demodulated
        return len(output_items[0])

