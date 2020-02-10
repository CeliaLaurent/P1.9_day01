import numpy as np
import sys
import matplotlib.pyplot as plt

xval=list(np.around(np.arange(-5.,5.,0.1),decimals=1))

if(len(sys.argv)!=2): 
    sys.exit()

fnum=sys.argv[1]

if(fnum=="1"):
  yval = list(map(lambda x: x , xval))
elif(fnum=="2"):
  yval = list(map(lambda x: x**2 , xval))
else:
  sys.exit()

plt.plot(xval,yval)
plt.show()
