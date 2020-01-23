# HP-OSA
Here is some python code to get spectra from an old HP 70950A optical spectrum analyzer (OSA) connected via GPIB.

You'll probably need to change the address of the OSA that is hard-coded into this script. Use 

    import visa
    rm = visa.ResourceManager()
    print(rm.list_resources()) 

to get the address of the OSA. 

You'll need some other software to run these scripts:

 - National instruments VISA:
       https://www.ni.com/en-us/support/downloads/drivers/download.ni-visa.html#329456
 - pyvisa:
       use the Anaconda Prompt and type "pip install pyvisa"
       https://pypi.org/project/PyVISA/
 - For the NI GPIB-to-USB converter, you need NI 488.2 driver
       https://www.ni.com/en-us/support/downloads/drivers/download.ni-488-2.html#329025

Please make a pull request if you make any improvements.

The HP_OPA.py script collects a single spectrum, while the "time series" script continuously collects spectra over time.

This is MIT licensed, so please do whatever you want with it.

Have fun!

Dan
