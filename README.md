# HP-OSA
Some python code to get spectra from an old HP 70950A optical spectrum analyzer (OSA)

These script are used to grab spectra from an HP OSA connected via GPIB. You'll probably need to change the address of the OSA that is hard-coded into this script. Use 

    import visa
    rm = visa.ResourceManager()
    print(rm.list_resources()) 

to get the address of the OSA. 

These scripts were run with Python2, so there are probably some print statements that need parentheses.

Pleaes make a pull request if you make any improvements.

This is MIT licensed, so please do whatever you want with it.

Have fun!

Dan
