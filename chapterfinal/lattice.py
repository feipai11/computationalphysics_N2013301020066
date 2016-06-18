import numpy as np
from pylab import *
import time 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import time

class Lattice:
    def __init__(self,m1=1.0,m2=1.0,K=1):       ### construct the dynamical matrix
        self.D=np.zeros((200,200))
        self.D=2*np.eye(200,k=0)-np.eye(200,k=100)-np.eye(200,k=99)-np.eye(200,k=-100)-np.eye(200,k=-99)
        self.D[99][0]=0
        self.D[99][99]=0
        self.D[100][199]=0
        self.D[100][199]=0
        self.D[0:100,:]=self.D[0:100,:]/m1*K
        self.D[100:200,:]=self.D[100:200,:]/m2*K
        self.w1=np.zeros(100)
        self.w2=np.zeros(100)
    def cal(self):
        w_2,b=np.linalg.eig(self.D)
        w=(np.sort(w_2).real)**0.5
        self.w1=w[0:99]
        self.w2=w[101:200]
    def re_plot(self):
        x1=pi*np.linspace(0,0.5,99)
        x2=pi*np.linspace(0.5,0,99)
        plot(x1,self.w1,'k:',label='Acoustic branch',lw=2)
        plot(x2,self.w2,'k',label='Optical branch',lw=2)
        xlabel('wave mode')
        ylabel('w')
        legend(loc='best',frameon=False)
        title(r'Dispersion relation of $\Gamma -X$')
        #show()
class two_dlattice:
    def __init__(self,m1=1.0,m2=8.0,K=1):         ### construct the dynamical matrix
        self.D=4*np.eye(900,k=0)-np.eye(900,k=1)-np.eye(900,k=-1)
        for i in range(self.D.shape[0]):
            for j in range(self.D.shape[1]):
                if j-i==30:
                    self.D[i][j]=-1
                if j-i==-30:
                    self.D[i][j]=-1
        self.f=[]
        m=[m1,m2]*450
        self.m=np.diag(np.array(m))
        self.D=dot(np.linalg.inv(self.m),self.D)
        print self.D

    def cal(self):
        w_2,b=np.linalg.eig(self.D)
        w=w_2**0.5
        w_a=np.sort(w)
        fig=figure(figsize=(10,4))
        ax=fig.add_subplot(1,2,1)
        scatter(np.linspace(0,899,900),w,s=2)
        title('dispersion relation of two dimentional lattice in <001> direction',fontsize=8)
        ax=fig.add_subplot(1,2,2)
        scatter(np.linspace(0,899,900),w_a,s=2)
        title('the w in the normal sequence',fontsize=8)
        show()
        f=np.zeros((30,30))
        for i in range(b.shape[0]):
            f=b[i].reshape(30,30)
            self.f.append(f)
    def fun_plot(self):
        x=np.linspace(0,30,30)
        y=np.linspace(0,30,30)
        X, Y = np.meshgrid(x, y)
        f1=np.outer(sin(pi/30*x),sin(pi/30*x))
        f2=np.outer(sin(pi/30*x),sin(2*pi/30*x))
        f3=np.outer(sin(2*pi/30*x),sin(2*pi/30*x))
        fig = plt.figure(figsize=(15,4))
        ax = fig.add_subplot(1,3,1,projection='3d')
        surf=ax.plot_surface(X,Y,f1,rstride=1, cstride=1,linewidth=0, antialiased=False,cmap=cm.coolwarm)
        title('eigenvectors of mode(1,1)')
        ax = fig.add_subplot(1,3,2,projection='3d')
        surf=ax.plot_surface(X,Y,f2,rstride=1, cstride=1,linewidth=0, antialiased=False,cmap=cm.coolwarm)
        title('eigenvectors of mode(1,2)')
        ax = fig.add_subplot(1,3,3,projection='3d')
        surf=ax.plot_surface(X,Y,f3,rstride=1, cstride=1,linewidth=0, antialiased=False,cmap=cm.coolwarm)
        title('eigenvectors of mode(1,1)')
        show()


start=time.clock()
fig=plt.figure(figsize=(15,8))
ax=fig.add_subplot(1,2,1)
a=Lattice(m1=2,m2=0.8)
a.cal()
b=Lattice(K=1.1)
b.cal()
x1=pi*np.linspace(0,0.5,99)
x2=pi*np.linspace(0.5,0,99)
plot(x1,a.w1,'k:',label='Acoustic branch',lw=2)
plot(x2,a.w2,'k',label='Optical branch',lw=2)
plot(x1,b.w1,'r:',label='Acoustic branch',lw=2)
plot(x2,b.w2,'r',label='Optical branch',lw=2)
xlabel('wave mode')
ylabel('w')
legend(loc='best',frameon=False)
title(r'Dispersion relation of $\Gamma -X$')
ax=fig.add_subplot(1,2,2)
c=Lattice(m1=1.2,m2=1.8)
c.cal()
d=Lattice(m2=2,K=0.9)
d.cal()
plot(x1,c.w1,'k:',label='Acoustic branch',lw=2)
plot(x2,c.w2,'k',label='Optical branch',lw=2)
plot(x1,d.w1,'r:',label='Acoustic branch',lw=2)
plot(x2,d.w2,'r',label='Optical branch',lw=2)
xlabel('wave mode')
ylabel('w')
legend(loc='best',frameon=False)
title(r'Dispersion relation of $\Gamma -L$')

show()
#b.re_plot()
#b=two_dlattice()
#b.cal()
#b.fun_plot#()
finish=time.clock()
print 'total time %12.1f s'%(finish-start)
