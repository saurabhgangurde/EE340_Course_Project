cmake ../
make
sudo make install
sudo ldconfig
sudo cp /usr/local/share/gnuradio/grc/blocks/gmsk_gmsk_py_cc.xml /usr/share/gnuradio/grc/blocks/gmsk_gmsk_py_cc.xml
sudo cp /usr/local/share/gnuradio/grc/blocks/gmsk_gmsk_demod_py_cc.xml /usr/share/gnuradio/grc/blocks/gmsk_gmsk_demod_py_cc.xml
sudo cp /usr/local/share/gnuradio/grc/blocks/gmsk_channel_est_py_ccc.xml /usr/share/gnuradio/grc/blocks/gmsk_channel_est_py_ccc.xml

