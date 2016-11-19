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

class gmsk_py_cc(gr.sync_block):
    """
    docstring for block gmsk_py_cc
    """
    def __init__(self):

        gr.sync_block.__init__(self,
            name="gmsk_py_cc",
            in_sig=[numpy.float32],
            out_sig=[numpy.complex64])



    def gaussian(self,in_signal):
        filtered=numpy.array([])
        filters.gaussian_filter(in_signal, 20, order=0, output=filtered)
        return filtered

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

        filters.gaussian_filter(in0, 6, order=0, output=in0)

        c_t=[0 for i in range(len(in0))]
        for i in range(len(in0)):
            c_t[i]=c_t[i-1]+in0[i]

        c_t=numpy.array(c_t)

        c_t=10*c_t/Fs
        print len(in0)


        out[:] = numpy.cos(c_t)+1j*numpy.sin(c_t)

        return len(output_items[0])

