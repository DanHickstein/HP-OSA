# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 12:24:11 2018

@author: dhickstein
"""
import numpy as np
import matplotlib.pyplot as plt
import os
import visa
import time

rm = visa.ResourceManager()
osa = rm.get_instrument("GPIB0::5::INSTR")

startWL = float(osa.query("STARTWL?"))
stopWL  = float(osa.query("STOPWL?"))
print startWL, stopWL
osa.timeout = 4000

folder = 'time_series'
fileformat = folder+'/%04i.txt'
delay = 60 # delay time in seconds



filenum=1
while True:
    if os.path.exists(fileformat%filenum):
        print 'exists'
        filenum += 1
    else:
        break


while True:
    print 'Collecting data...'
    data = osa.query("TRDEF TRA, 2048; TRA?;").rstrip().split(',')
    data = np.array([float(num) for num in data])
    
    print 'saving ' + fileformat%filenum

    wls = np.linspace(startWL, stopWL, data.shape[0])

    with open(fileformat%filenum, 'w') as outfile:
        for wl, d in zip(wls, data):
            outfile.write('%f, %f\n'%(wl*1e9,d))
    
    print 'waiting %i seconds'%delay
    time.sleep(delay)
    filenum += 1
    
#plt.show()


