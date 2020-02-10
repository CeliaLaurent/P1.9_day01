import numpy as np
import sys
import matplotlib.pyplot as plt

def usage():
    print("Usage: this scripts takes one <int> argument and plots different functions:")
    print(" - 'python script.py 1' plots y=x")
    print(" - 'python script.py 2' plots y=x**2")
    print(" - 'python script.py 3' plots y=x**3")

xval=list(np.around(np.arange(-3.,3.,0.1),decimals=1))

if(len(sys.argv)!=2): 
    usage()
    sys.exit()

fnum=sys.argv[1]

if(fnum=="1"):
    yval = list(map(lambda x: x , xval))
elif(fnum=="2"):
    yval = list(map(lambda x: x**2 , xval))
elif(fnum=="3"):
    yval = list(map(lambda x: x**3 , xval))
else:
    usage()
    sys.exit()

plt.plot(xval,yval)
plt.show()
