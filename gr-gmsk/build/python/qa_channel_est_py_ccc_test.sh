#!/bin/sh
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/saurabh/Desktop/EE340_Course_Project/gr-gmsk/python
export PATH=/home/saurabh/Desktop/EE340_Course_Project/gr-gmsk/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$DYLD_LIBRARY_PATH
export DYLD_LIBRARY_PATH=$LD_LIBRARY_PATH:$DYLD_LIBRARY_PATH
export PYTHONPATH=/home/saurabh/Desktop/EE340_Course_Project/gr-gmsk/build/swig:$PYTHONPATH
/usr/bin/python2 /home/saurabh/Desktop/EE340_Course_Project/gr-gmsk/python/qa_channel_est_py_ccc.py 
