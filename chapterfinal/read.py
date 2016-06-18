import numpy as np
from pylab import *
a=np.loadtxt('wavefun0.dat')
for i in range(1,6):
    plot(a[:,0],a[:,i],label='mode n=%d'%i)
    xlabel(r'$x$')
    ylabel(r'$\psi (x)$')
    title('first 5 wave function of radial equation of hydrogen atom',fontsize=10)
    legend(loc='best',frameon=False,prop={'size':10})
    xlim([0,15])
show()
