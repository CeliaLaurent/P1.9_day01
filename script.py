import numpy as np
import sys

xval=list(np.around(np.arange(-5.,5.,0.1),decimals=1))

if(len(sys.argv)!=2): 
    sys.exit()

fnum=sys.argv[1]
