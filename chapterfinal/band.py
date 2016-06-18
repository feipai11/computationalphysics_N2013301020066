import numpy as np
from pylab import *
import time

class Band:
    def __init__(self,A=-10,a=0.1):                #### contruct the potential in x-space and the matrix element in the equation
        self.kh=pi/2*np.linspace(0,99,500)        #### here we use 500 plane wave to calculate the band structure
        self.k=pi/200*np.linspace(0,149,150)         #### the potential can be changed and the parameters A and a can be optimize
        self.e=[]
        self.x=np.linspace(-1,1,1000)
        self.u=np.zeros(1000)
        for i in range(len(self.x)):
            self.u[i]=np.where(abs(self.x[i])<a,A,-abs(self.x[i])**(-1))
        self.f=np.fft.rfft(self.u).real/1000
        self.fi=abs(np.fft.irfft(self.u)).real/1000
        #print self.f
        #plot(self.kh,self.f[0:len(self.kh)],'r')
        #plot(self.kh,self.fi[0:len(self.kh)]-np.ones(len(self.kh)),'g')
        #show()

    def matrax(self):                               ##### construct the Matrix in k-space, the matrix is like the paper have said.
        for i in range(len(self.k)):
            h=np.diag(1e-3*(self.kh+self.k[i]*np.ones(1000))**2)
            for j in range(h.shape[0]):
                for k in range(h.shape[1]):
                    if k-j==1:
                        h[j][k]=-2*h[1][1]
                    if k-j==-1:
                        h[j][k]=-2*h[1][1]
            a,b=np.linalg.eig(h)                    #### solve the eigenvalue equation, the eigenvale is the energy of each k
            self.e.append(np.sort(a))
    def band_plot(self):                            #### plot the band structure
        for i in range(len(self.e)):
            scatter(self.k[i]*np.ones(2),self.e[i][0:2],s=2)         #### plot only the first two band
        xlabel('k')
        ylabel('energy')
        xlim([0,2.4])
        title('Band structure')
        show()

start=time.clock()        

a=Band()

a.matrax()
finish=time.clock()
print 'consume time %f s'%(finish-start)
a.band_plot()

