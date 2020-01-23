"""
Created on Tue Sep 25 12:24:11 2018

@author: Dan Hickstein (danhickstein@gmail.com)

This script grabs a spectrum from an HP 70950A optical spectrum analyzer (OSA)
You'll need to manually change the "osa_address" variable to match the actual
GPIB address of your OSA.

Requirements:
 - National instruments VISA:
       https://www.ni.com/en-us/support/downloads/drivers/download.ni-visa.html#329456
 - pyvisa:
       use the Anaconda Prompt and type "pip install pyvisa"
       https://pypi.org/project/PyVISA/
 - For the GPIB-to-USB converter, you need NI 488.2 driver
       https://www.ni.com/en-us/support/downloads/drivers/download.ni-488-2.html#329025

version 0.1.5 - 2020-01-23
    - made py3 compatible
version 0.1.4 
    - uploaded to github
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import visa

rm = visa.ResourceManager()

print('Devices found:')
print(rm.list_resources())  # use this to figure out the address of the OSA
print('Connecting to OSA...')

# --- CHANGE THIS TO MATCH YOUR OSA:
osa_address = "GPIB0::5::INSTR"
# ----------------------------------

print('Trying to connect to %s' % osa_address)
osa = rm.get_instrument(osa_address)

startWL = float(osa.query("STARTWL?"))
stopWL = float(osa.query("STOPWL?"))
print('Wavelength range: %.1f to %.1f nm' % (startWL*1e9, stopWL*1e9))
osa.timeout = 4000

print('Grabbing data from OSA...')
data = osa.query("TRDEF TRA, 2048; TRA?;").rstrip().split(',')
data = np.array([float(num) for num in data])

wls = np.linspace(startWL, stopWL, data.shape[0])

plt.plot(wls*1e9, data)

prefix = 'spec'
fileformat = prefix+'%04i.txt'

filenum = 1
while True:
    if os.path.exists(fileformat % filenum):
        filenum += 1
    else:
        break

print('Saving ' + fileformat % filenum + '...')

with open(fileformat % filenum, 'w') as outfile:
    for wl, d in zip(wls, data):
        outfile.write('%f, %f\n' % (wl*1e9, d))

print('================== Finished! ================')
