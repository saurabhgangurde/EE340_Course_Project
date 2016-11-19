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

class channel_est_py_ccc(gr.sync_block):
    """
    docstring for block channel_est_py_ccc
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name="channel_est_py_ccc",
            in_sig=[numpy.complex64,numpy.complex64],
            out_sig=[numpy.complex64])


    def work(self, input_items, output_items):
        in0 = input_items[0]
        in1 = input_items[1]
        out = output_items[0]
        # <+signal processing here+>

        
        h=0
        for i in range(len(in0)):
            h+=in0[i]/in1[i]
        h/=len(in0)
        temp=numpy.ones(len(in0))*h
        out[:] = temp
        return len(output_items[0])
        

