# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 12:24:11 2018

@author: dhickstein
"""
import numpy as np
import matplotlib.pyplot as plt
import os
import visa

rm = visa.ResourceManager()
#print dir(rm)
print rm.list_resources() # use this to figure out the address of the OSA
print('Connecting to OSA...')
osa = rm.get_instrument("GPIB0::5::INSTR")

startWL = float(osa.query("STARTWL?"))
stopWL  = float(osa.query("STOPWL?"))
print('Wavelength range: %.1f to %.1f nm'%(startWL*1e9, stopWL*1e9))
osa.timeout = 4000

print('Grabbing data from OSA...')
data = osa.query("TRDEF TRA, 2048; TRA?;").rstrip().split(',')
data = np.array([float(num) for num in data])

wls = np.linspace(startWL, stopWL, data.shape[0])

plt.plot(wls*1e9,data)

prefix = 'spec'
fileformat = prefix+'%04i.txt'

filenum=1
while True:
    if os.path.exists(fileformat%filenum):
        filenum += 1
    else:
        break

print 'Saving ' + fileformat%filenum + '...'
with open(fileformat%filenum, 'w') as outfile:
    for wl, d in zip(wls, data):
        outfile.write('%f, %f\n'%(wl*1e9,d))
        
print '================== Finished! ================'
    
#plt.show()


